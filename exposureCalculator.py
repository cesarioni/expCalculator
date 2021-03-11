import maya.cmds
import functools
import math 

def createUI(pWindowTitle, pApplyCallback):
    windowCalcID = 'myWindowCalcID'
    if cmds.window(windowCalcID, exists = True):
        cmds.deleteUI( windowCalcID )
    cmds.window( windowCalcID, title = pWindowTitle, resizeToFitChildren = True, width = 500)
    cmds.rowColumnLayout( numberOfColumns = 2, columnWidth = [(1, 100),(2,100)], columnOffset = [ (1, 'left', 3) ] )
 
    
    cmds.text ( label = 'Intensity' )
    cmds.text ( label = 'Exposure' )
    
    intValue = cmds.floatField (value = 1)
    expValue = cmds.floatField (value = 0)
    
    cmds.button ( label = 'GET intensity', command = functools.partial( transExpIntCallback, intValue,  expValue) )
    cmds.button ( label = 'GET Exposure', command = functools.partial( transIntExpCallback, intValue,  expValue) )
    
    
    cmds.showWindow()
                       
                     
def transIntExpCallback (intValue,expValue,*pArgs ):
    intVal = cmds.floatField(intValue, query = True, value = True)
    expVal = cmds.floatField(expValue, query = True, value = True)
    totalInt = intVal *( 2**expVal )
    newExpVal =  math.log(totalInt,2)
    cmds.floatField(expValue, edit = True, value = newExpVal)
        

def transExpIntCallback (intValue,expValue,*pArgs ):
    intVal = cmds.floatField(intValue, query = True, value = True)
    expVal = cmds.floatField(expValue, query = True, value = True)
    totalInt = intVal *( 2**expVal )
    newIntVal =  totalInt /( 2**expVal )
    cmds.floatField(intValue, edit = True, value = totalInt)

createUI( 'light group selector', applyCallback )
     
        
cmds.select( clear=True )