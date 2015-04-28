# 3D齒輪creo繪圖方法(負責人:40223110王常浩)

說明 Brython 協同繪圖模式下, 與 JavaScript canvas 繪圖對應的相關概念與可用指令

我們需要在協同中繪製圖形可以與JavaScript canvas對應的相關指令，讓我們可以順利的畫出齒輪

首先先設定

<script src="/static/Cango2D.js" type="text/javascript"></script>

<script src="/static/gearUtils-04.js" type="text/javascript"></script>

將type="text/javascript"改成javascript這樣就可以在Brython協同繪圖模式執行並將畫布設定為"2d"

畫布 = document["plotarea"]

ctx = 畫布.getContext("2d")



1.畫圓
```
ctx.beginPath() 
#開始畫布
ctx.lineWidth = 3 
#線條大小為3
ctx.strokeStyle = "black" 
#線條的顏色為"黑色"
ctx.arc(250,250,50,0,2*math.pi)  
#在畫布的x=250 y=250 半徑為50
ctx.stroke() 
#結束畫布
```


2.畫直線
```
ctx.beginPath() 
#開始畫布
ctx.lineWidth = 3 
#線條大小為3
ctx.moveTo(0, 0)  
#從x=0 y=0座標
ctx.lineTo(500, 0) 
#到x=500 y=0 座標
ctx.strokeStyle = "blue" 
#線條的顏色為"藍色"
ctx.stroke() 
#結束畫布
```



3.畫圖塊，先用上面畫三角形
```
ctx.beginPath() 
#開始畫布
ctx.moveTo(20,20) 
#從x=20 y=20座標
ctx.lineTo(20,100) 
#到x=20 y=100 座標
ctx.lineTo(70,100) 
#再到x=70 y=100 座標
ctx.stroke() 
#結束畫布
ctx.fillStyle="green" 
#用綠色填滿圖形
ctx.fill() 
#全部填滿
```


備註:若要讓圖形旋轉可用旋轉指令

ctx.rotate(45 * Math.PI / 180)此為轉動45度

#分組任務_Pro/Web.Link 程式結合
```
@cherrypy.expose
def cube_weblink(self):
    outstring = '''<script type="text/javascript" src="/static/weblink/pfcUtils.js"></script>
<script type="text/javascript" src="/static/weblink/wl_header.js">
document.writeln ("Error loading Pro/Web.Link header!");
</script>
<script type="text/javascript" language="JavaScript">
// 若第三輸入為 false, 表示僅載入 session, 但是不顯示
// ret 為 model open return
 var ret = document.pwl.pwlMdlOpen("cube.prt", "v:/tmp", false);
if (!ret.Status) {
    alert("pwlMdlOpen failed (" + ret.ErrorCode + ")");
}
    //將 ProE 執行階段設為變數 session
    var session = pfcGetProESession();
    // 在視窗中打開零件檔案, 並且顯示出來
    var window = session.OpenFile(pfcCreate("pfcModelDescriptor").CreateFromFileName("cube.prt"));
    
    var solid = session.GetModel("cube.prt",pfcCreate("pfcModelType").MDL_PART);
    
    var length,width,myf,myn,i,j,volume,count,d1Value,d2Value;
    
    // 將模型檔中的 length 變數設為 javascript 中的 length 變數
    length = solid.GetParam("a1");
    // 將模型檔中的 width 變數設為 javascript 中的 width 變數
    width = solid.GetParam("a2");
//改變零件尺寸
    //myf=20;
    //myn=20;
    volume=0;
    count=0;
    try
    {
            // 以下採用 URL 輸入對應變數
            //createParametersFromArguments ();
            // 以下則直接利用 javascript 程式改變零件參數
            for(i=0;i<=1;i++)
            {
                //for(j=0;j<=2;j++)
                //{
                    myf=20.0;
                    myn=10.0+i*0.5;
// 設定變數值, 利用 ModelItem 中的 CreateDoubleParamValue 轉換成 Pro/Web.Link 所需要的浮點數值
         d1Value = pfcCreate ("MpfcModelItem").CreateDoubleParamValue(myf);
         d2Value = pfcCreate ("MpfcModelItem").CreateDoubleParamValue(myn);
// 將處理好的變數值, 指定給對應的零件變數
                    length.Value = d1Value;
                    width.Value = d2Value;
                    //零件尺寸重新設定後, 呼叫 Regenerate 更新模型
                    solid.Regenerate(void null);
                    //利用 GetMassProperty 取得模型的質量相關物件
                    properties = solid.GetMassProperty(void null);
                    //volume = volume + properties.Volume;
volume = properties.Volume;
                    count = count + 1;
alert("執行第"+count+"次,零件總體積:"+volume);
// 將零件存為新檔案
var newfile = document.pwl.pwlMdlSaveAs("cube.prt", "v:/tmp", "cube"+count+".prt");
if (!newfile.Status) {
    alert("pwlMdlSaveAs failed (" + newfile.ErrorCode + ")");
}
//} // 內圈 for 迴圈
            } //外圈 for 迴圈
            //alert("共執行:"+count+"次,零件總體積:"+volume);
            //alert("零件體積:"+properties.Volume);
            //alert("零件體積取整數:"+Math.round(properties.Volume));
        }
    catch(err)
        {
            alert ("Exception occurred: "+pfcGetExceptionType (err));
        }
</script>
'''
    return outstring
```

將齒數、模數、壓力角把它們找出來之後，並把length 設定為齒數

m 設定成壓力角
```
  // 將模型檔中的 length 變數設為 javascript 中的 length 變數
    npinion = solid.GetParam("n");
    // 將模型檔中的 width 變數設為 javascript 中的 width 變數
    width = solid.GetParam("face_width");
    m = solid.GetParam("module");
```
