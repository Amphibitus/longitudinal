# -*- coding: utf-8 -*-
"""
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from __future__ import print_function
from builtins import str
from builtins import object

import locale

from qgis.PyQt.QtWidgets import *

from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.core import *
from qgis.gui import *

try:
    from pyspatialite import dbapi2 as db
except:
    QgsMessageLog.logMessage('pyspatialite')

class spatialiteManager(object):
    def __init__(self, dbase):
        # get a connection, if a connect cannot be made an exception will be raised here
        self.conn = db.connect(dbase)
        self.cur = self.conn.cursor()

    def createDB(self):
        # initializing Spatial MetaData
        # using v.2.4.0 this will automatically create
        # GEOMETRY_COLUMNS and SPATIAL_REF_SYS
        sql = 'SELECT InitSpatialMetadata()'
        self.query(sql)

    def query(self, sql):
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur
        
    def spatialIndex(self, table, geomCol):
        sql = """SELECT CreateSpatialIndex('{0}', '{1}')""".format(table, geomCol)
        self.cur.execute(sql)
        self.conn.commit()
        
    def removeSpatialIndex(self, table, geomCol):
        sql = """SELECT DisableSpatialIndex('{0}', '{1}')""".format(table, geomCol)
        self.cur.execute(sql)
        self.conn.commit()
        sql = """DROP TABLE idx_{}_{}""".format(table, geomCol)
        self.cur.execute(sql)
        self.conn.commit()       

    def dropTables(self,tables):
        for i in tables:
            sql = '''DROP TABLE IF EXISTS {}'''.format(i)
            self.cur.execute(sql)
            self.conn.commit()        
        self.cur.execute('VACUUM')
        self.conn.commit()
        
    def discardGeom(self, table, geomCol):
        sql = """SELECT DiscardGeometryColumn('{}', '{}')""".format(table, geomCol)
        self.cur.execute(sql)
        self.conn.commit()

    def __del__(self):
        # fix_print_with_import
        print('close db')
        self.conn.close() 

  
def createDB(layer, dbase, srid):
    # setup spatilite manager
    dbmgr = spatialiteManager(dbase)
    # create database
    dbmgr.createDB()
    # for custom CRS,  check if projection doesn't exist in spatialite database
    sql = """SELECT COUNT(*) FROM spatial_ref_sys WHERE srid = {}""".format(srid)
    count = dbmgr.query(sql).fetchall()[0][0]
    if count == 0: # add def. if needed
        sql = """INSERT INTO spatial_ref_sys(srid, auth_name, auth_srid, ref_sys_name, proj4text, srtext) VALUES({0}, '', '', '{3}', '{1}', '{2}')""".format(srid, layer.crs().toProj4(), layer.crs().toWkt(), layer.crs().description())
        dbmgr.query(sql)
        customCRSFlag = True  
    else:
        customCRSFlag = False
    return customCRSFlag
  
def loadVectorsIntoDB(layers, dbase, customCRSFlag, srid):
    #database import options
    options = {}
    options['overwrite'] = True
    options['forceSinglePartGeometryType'] = True
    uri = QgsDataSourceURI()
    uri.setDatabase(dbase)
    for layer in layers:
        uri.setDataSource('',layer.name(),'the_geom')
        ret, errMsg = QgsVectorLayerImport.importLayer(layer, uri.uri(), 'spatialite', layer.crs(), False, False, options)
        
        ## for custom CRS
        if customCRSFlag:
            dbmgr = spatialiteManager(dbase)
            sql = """UPDATE geometry_columns SET srid = {} WHERE f_table_name = '{}'""".format(srid, layer.name().lower())
            dbmgr.query(sql)
            sql = """UPDATE {} SET the_geom = SetSRID(the_geom, {})""".format(layer.name(), srid)
            dbmgr.query(sql)



def getPointLayerNames():
    layerMap = QgsProject.instance().mapLayers()
    layerNames = []
    for name, layer in layerMap.items():
        if layer.type() == QgsMapLayer.VectorLayer and layer.geometryType()==QgsWkbTypes.PointGeometry:
            layerNames.append(str(layer.name()))
    return sorted(layerNames)#, cmp=locale.strcoll)
    
def getLineLayerNames():
    layerMap = QgsProject.instance().mapLayers()
    layerNames = []
    for name, layer in layerMap.items():
        if layer.type() == QgsMapLayer.VectorLayer and layer.geometryType()==QgsWkbTypes.LineGeometry:
            layerNames.append(str(layer.name()))
    return sorted(layerNames)#, cmp=locale.strcoll)


def getVectorLayerByName(layerName):
    layerMap = QgsProject.instance().mapLayers()
    for name, layer in layerMap.items():
        if layer.type() == QgsMapLayer.VectorLayer and layer.name() == layerName:
            if layer.isValid():
                return layer
            else:
                return None


def getFieldNames(layer, fieldTypes):
    fields = layer.fields()
    fieldNames = []
    for field in fields:
        if field.type() in fieldTypes and not field.name() in fieldNames:
            fieldNames.append(str(field.name()))
    return fieldNames


def getFieldType(layer, fieldName):
    fields = layer.fields()
    for field in fields:
        if field.name() == fieldName:
            return field.typeName()


def getUniqueValuesCount(layer, fieldIndex, useSelection):
    count = 0
    values = []
    if useSelection:
        for f in layer.selectedFeatures():
            if f[fieldIndex] not in values:
                values.append(f[fieldIndex])
                count += 1
    else:
        request = QgsFeatureRequest().setFlags(QgsFeatureRequest.NoGeometry)
        for f in layer.getFeatures(request):
            if f[fieldIndex] not in values:
                values.append(f[fieldIndex])
                count += 1
    return count

def checkMultipart(layer):
    for f in layer.getFeatures():
        if f.geometry().isMultipart():
            return True
    return False



def getSaveFileName(parent, caption, directory, filter):
    """Qt4/Qt5 compatible getSaveFileName"""
    fileName = QFileDialog.getSaveFileName(parent = parent,
                                        caption = caption,
                                        directory = directory,
                                        filter = filter)
    if isinstance(fileName, tuple):  #pyqt5 case
        fileName = fileName[0]
    return fileName


# get geometry from different geometry types
def get_geometry (fg):
    # test for multilinestring
    if fg.wkbType() == 5 or fg.wkbType() == 1005: 
        nodes = fg.asMultiPolyline()[0]
        return nodes
                    
    # test for linesting
    if fg.wkbType() == 2  or fg.wkbType() == 1002:
        nodes = fg.asPolyline()
        return nodes

# selected length and count            
def getLength(layer):
    totalLen = 0
    count = 0
    for feature in layer.selectedFeatures():
        geom = feature.geometry()
#            idtxt = feature[str(self.dock.comboFields.currentText())]
#            self.dock.textEditLog.append(idtxt)
        totalLen = totalLen + geom.length()
        count = count + 1
    return totalLen, count


def getdist(p1,p2):
    x=(((p2.x()-p1.x())**2)+((p2.y()-p1.y())**2))**0.5
    return  x

    

def float_de(s):
    if s.strip()=='':
        s='0'

    if s.find(",")>0:
        s = s.replace('.','').replace(',','.')

    try:
        a = float(s)
    except ValueError:
        #QgsMessageLog.logMessage("String :"+str(s)+" ist keine Zahl", 'M150xml', Qgis.Warning)
        a = 0
    return a



def value_de(s):
    s=str(s)
    if s.strip()=='' or s == 'None':
        s='0'

    if s.find(".")>0:
        s = s.replace('.',',')

    try:
        a = s
    except ValueError:
        #QgsMessageLog.logMessage("String :"+str(s)+" ist keine Zahl", 'M150xml', Qgis.Warning)
        a = '0'
    return a

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        
# Suche alle linien, die miteinander verküpft sind (funktioniert nach unten, aber auch nach oben)
def selectDownstream(layer,sourceFeatID,tolerance,uIdirection):
    global totallength
    proj = QgsProject.instance()
    
    # distance = 0
    
    #setup distance
    distance = QgsDistanceArea()
    # the unit of measure will be set to the same as the layer
    # maybe it would be better to set it to the map CRS
    distance.setSourceCrs(layer.sourceCrs(), QgsProject.instance().transformContext())
        

    # get crs for tolerance setting
    crs = layer.crs().authid()

    # setup total length
    totallength = 0.0        
    # print (crs)
    if crs == 'EPSG:4269':
        rec = .0001
        
    else:
        #rec = .1
        rec = tolerance

    selection_list = []
    final_list = []
    layer.removeSelection()
    
    layer.select(sourceFeatID)
    provider = layer.dataProvider()
    
    selection_list.append(sourceFeatID)
    final_list.append(sourceFeatID)
    
    # this part partially based on flowTrace by "Ed B"
    #loop thru selection list
    while selection_list:
        
        #get selected features
        request = QgsFeatureRequest().setFilterFid(selection_list[0])
        # request = QgsFeatureRequest()
        feature = next(layer.getFeatures(request))
        geom = feature.geometry()

        # get nodes
        nodes = get_geometry (feature.geometry())

        
        # get upstream node
        if uIdirection :
            upstream_coord = nodes[-1]
            # print (upstream_coord)
        else:
            upstream_coord = nodes[0]
            # print (upstream_coord)
            
        # select all features around upstream coordinate 
        # using a bounding box
        rectangle = QgsRectangle(upstream_coord.x() - rec/2, 
                        upstream_coord.y() - rec/2, 
                        upstream_coord.x() + rec/2, 
                        upstream_coord.y() + rec/2)
        # rectangle = QgsRectangle (minx, miny, maxx, maxy)
        request = QgsFeatureRequest().setFilterRect(rectangle)
        features = layer.getFeatures(request)
        

        #iterate thru requested features
        for feature in features:
            # get nodes
            nodes = get_geometry (feature.geometry())
            #downstream_coord = nodes[-1]
            
            # get upstream node
            if uIdirection:
                downstream_coord = nodes[0]
                # print (upstream_coord)
            else:
                downstream_coord = nodes[-1]
                # print (upstream_coord)
            

            
            #get distance from downstream node to upstream node
            dist = distance.measureLine(downstream_coord,upstream_coord)
            
            if dist < tolerance:
                #add feature to final list
                final_list.append(feature.id())
                
                if feature.id() not in selection_list:
                    #add feature to selection list
                    selection_list.append(feature.id())
                    # Length from Line                            
                    totallength +=  distance.measureLength(feature.geometry())
                    
        
        
        #remove feature from selection list
        selection_list.pop(0)
            
    #select features using final_list           
    layer.selectByIds(final_list)
    tot = getLength(layer)
    
    #self.uSelectedLine.setText('Now selected Lines '+ str(len(final_list)))


# Suche alle linien, die miteinander verküpft sind (funktioniert nach unten, aber auch nach oben)
def Linesorted(layer, selection_list,tolerance,uIdirection):
    

    #setup distance
    distance = QgsDistanceArea()
    # the unit of measure will be set to the same as the layer
    # maybe it would be better to set it to the map CRS
    distance.setSourceCrs(layer.sourceCrs(), QgsProject.instance().transformContext())
        

    # get crs for tolerance setting
    crs = layer.crs().authid()
    if crs == 'EPSG:4269':

        tolerance = .0001
 

    provider = layer.dataProvider()

    # erstmal nach oben
    for feature in  selection_list:
        print ('Starte mit:'+repr(str(feature.id())),end='')
        # get upper nodes
        nodes = get_geometry (feature.geometry())
        upstream_coord = nodes[0]
        top_feature=''
        for featuresearch in  selection_list:
            if featuresearch.id != feature.id:
                 # get under  nodes
                nodes = get_geometry (featuresearch.geometry())
                downstream_coord = nodes[-1]
           
                if  distance.measureLine(downstream_coord, upstream_coord)<=tolerance:
                    print ('Oben gefunden:'+repr(str(featuresearch.id())))
                    top_feature=featuresearch
                    break
        if top_feature=='':
            break
    final_list = []
    
     # und jetzt nach unten
    print ('Anfangshaltung:'+repr(str(feature.id())))
    while selection_list:
        final_list.append(feature)
        
        #remove feature from selection list
        selection_list.pop(selection_list.index(feature))

        print ('Starte mit:'+repr(str(feature.id())),end='')
        # get upper nodes
        nodes = get_geometry (feature.geometry())
        downstream_coord = nodes[-1] 
       
        for featuresearch in  selection_list:
            if featuresearch.id != feature.id:
                 # get under  nodes
                nodes = get_geometry (featuresearch.geometry())
                upstream_coord = nodes[0]
           
                if  distance.measureLine(downstream_coord, upstream_coord)<=tolerance:
                    print ('Unten gefunden:'+repr(str(featuresearch.id())))
                    feature=featuresearch
                    break

    
    return final_list


def selectPointFeaturefromlineFeature(LineLayer,lineFeature,pointLayer, tolerance):
    
    pfinal_list=[]
    pfeaturesUp=None
    pfeaturesDown=None 
    pfeatureUp=None
    pfeatureDown=None 
    
    # get crs for tolerance setting
    crs = LineLayer.crs().authid()
      
    # print (crs)
    if crs == 'EPSG:4269':
        rec = .0001
    else:
        #rec = .1
        #rec = self.spinBoxTol.value()
        rec = tolerance


    # get nodes
    nodes = get_geometry (lineFeature.geometry())
    upstream_coord = nodes[0]

    # select all features around upstream coordinate 
    # using a bounding box
    rectangle = QgsRectangle(upstream_coord.x() - rec/2, 
                    upstream_coord.y() - rec/2, 
                    upstream_coord.x() + rec/2, 
                    upstream_coord.y() + rec/2)
    # rectangle = QgsRectangle (minx, miny, maxx, maxy)
    request = QgsFeatureRequest().setFilterRect(rectangle)
    pfeaturesUp = pointLayer.getFeatures(request)
    for feature in pfeaturesUp:
        pfeatureUp=feature
        

    downstream_coord = nodes[-1]
    # select all features around upstream coordinate 
    # using a bounding box
    rectangle = QgsRectangle(downstream_coord.x() - rec/2, 
                    downstream_coord.y() - rec/2, 
                    downstream_coord.x() + rec/2, 
                    downstream_coord.y() + rec/2)
    # rectangle = QgsRectangle (minx, miny, maxx, maxy)
    request = QgsFeatureRequest().setFilterRect(rectangle)
    pfeaturesDown = pointLayer.getFeatures(request)
    for feature in pfeaturesDown:
        pfeatureDown=feature

    return pfeatureUp,pfeatureDown


