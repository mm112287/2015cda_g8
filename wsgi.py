# coding=utf-8
# 上面的程式內容編碼必須在程式的第一或者第二行才會有作用

################# (1) 模組導入區
# 導入 cherrypy 模組, 為了在 OpenShift 平台上使用 cherrypy 模組, 必須透過 setup.py 安裝



import cherrypy
# 導入 Python 內建的 os 模組, 因為 os 模組為 Python 內建, 所以無需透過 setup.py 安裝
import os
# 導入 random 模組
import random
# 導入 gear 模組
import gear
import legoman
################# (2) 廣域變數設定區
# 確定程式檔案所在目錄, 在 Windows 下有最後的反斜線
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
# 設定在雲端與近端的資料儲存目錄
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示程式在雲端執行
    download_root_dir = os.environ['OPENSHIFT_DATA_DIR']
    data_dir = os.environ['OPENSHIFT_DATA_DIR']
else:
    # 表示程式在近端執行
    download_root_dir = _curdir + "/local_data/"
    data_dir = _curdir + "/local_data/"

'''以下為近端 input() 與 for 迴圈應用的程式碼, 若要將程式送到 OpenShift 執行, 除了採用 CherryPy 網際框架外, 還要轉為 html 列印
# 利用 input() 取得的資料型別為字串
toprint = input("要印甚麼內容?")
# 若要將 input() 取得的字串轉為整數使用, 必須利用 int() 轉換
repeat_no = int(input("重複列印幾次?"))
for i in range(repeat_no):
    print(toprint)
'''
################# (3) 程式類別定義區
# 以下改用 CherryPy 網際框架程式架構
# 以下為 Hello 類別的設計內容, 其中的 object 使用, 表示 Hello 類別繼承 object 的所有特性, 包括方法與屬性設計
class Hello(object):

    # Hello 類別的啟動設定
    _cp_config = {
    'tools.encode.encoding': 'utf-8',
    'tools.sessions.on' : True,
    'tools.sessions.storage_type' : 'file',
    #'tools.sessions.locking' : 'explicit',
    # session 以檔案儲存, 而且位於 data_dir 下的 tmp 目錄
    'tools.sessions.storage_path' : data_dir+'/tmp',
    # session 有效時間設為 60 分鐘
    'tools.sessions.timeout' : 60
    }

    # 以 @ 開頭的 cherrypy.expose 為 decorator, 用來表示隨後的成員方法, 可以直接讓使用者以 URL 連結執行
    @cherrypy.expose
    # index 方法為 CherryPy 各類別成員方法中的內建(default)方法, 當使用者執行時未指定方法, 系統將會優先執行 index 方法
    # 有 self 的方法為類別中的成員方法, Python 程式透過此一 self 在各成員方法間傳遞物件內容
    def index_orig(self, toprint="Hello World!"):
        return toprint
    def __init__(self):
        # 配合透過案例啟始建立所需的目錄
        if not os.path.isdir(data_dir+'/tmp'):
            os.mkdir(data_dir+'/tmp')
        if not os.path.isdir(data_dir+"/downloads"):
            os.mkdir(data_dir+"/downloads")
        if not os.path.isdir(data_dir+"/images"):
            os.mkdir(data_dir+"/images")
    @cherrypy.expose
    def hello(self, toprint="Hello World!"):
        return toprint
    @cherrypy.expose
    def index(self, K=None, N=None, inp2=None):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.0-20150301-090019/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">
        協同產品設計，第八組<br/>
    <a href="legoman">樂高機器人組立</a><br/> 
    <table border=3>
    <tr>
    <th><font size="4">小組名單</font></th>
    <th><font size="4"></font></th>
    </tr>
    <tr rowspan="2">
    <th><font size='4' color='yellow' ><a href="index3">40223151簡正斌</a> </font></th>
    <th><font size="4"><a href="http://cd0427-40223110.rhcloud.com/">40223110王常浩</a></font></th>
    </tr>
    <tr>
    <th><font size="4"><a href="index2">40223124袁丞宗 </a></font></th>
    <th><font size="4"><a href="s40223129">40223129許家瑋 </a></font></th>
    </tr>
    <tr>
    <th><font size='4' color='yellow' ><a href="http://2015springcda-40223149.rhcloud.com/">40223149賴涵餘</a></font></th>
    <th><font size="4">40223150謝俊宇 </font></th>
    </tr><tr>
    <th><font size="4">40223145劉兆銓</font></th>
    <th></th>
    </tr>


        '''
        return outstring



    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def s40223129(self, m=None, ng1=None, inp2=None):
        # 將標準答案存入 answer session 對應區
        theanswer = random.randint(1, 100)
        thecount = 0
        # 將答案與計算次數變數存進 session 對應變數
        cherrypy.session['answer'] = theanswer
        cherrypy.session['count'] = thecount
        # 印出讓使用者輸入的超文件表單
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.0-20150301-090019/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">


    <form method=\"post\" action=\"gear4\">
        <fieldset>
        <legend>40223129的7顆齒輪嚙合參數表單(會畫圖):</legend>
        齒數1:<br />
        <input type=\"text\" name=\"ng1\"><br />
        齒數2:<br />
        <input type=\"text\" name=\"ng2\"><br />
        齒數3:<br />
        <input type=\"text\" name=\"ng3\"><br />
        齒數4:<br />
        <input type=\"text\" name=\"ng4\"><br />
        齒數5:<br />
        <input type=\"text\" name=\"ng5\"><br />
        齒數6:<br />
        <input type=\"text\" name=\"ng6\"><br />
        齒數7:<br />
        <input type=\"text\" name=\"ng7\"><br />
        </select>
        模數:<br />
        <input type=\"text\" name=\"m\"><br />
        壓力角(>33時會有錯誤):<br />
        <input type=\"text\" name=\"inp2\"><br />
        <input type=\"submit\" value=\"gear4\">
        <input type=\"reset\" value=\"重填\">
    </form>
    <hr>
    <!-- 以下在網頁內嵌 Brython 程式 -->
    <script type="text/python">
    from browser import document, alert

    def echo(ev):
        alert(document["zone"].value)

    # 將文件中名稱為 mybutton 的物件, 透過 click 事件與 echo 函式 bind 在一起
    document['mybutton'].bind('click',echo)
    </script>

    <!-- 以下為 canvas 畫圖程式 -->
    <script type="text/python">
    # 從 browser 導入 document
    from browser import document
    from math import *

    # 準備在 id="plotarea" 的 canvas 中繪圖
    canvas = document["plotarea"]
    ctx = canvas.getContext("2d")

    def create_line(x1, y1, x2, y2, width=3, fill="red"):
    ctx.beginPath()
    ctx.lineWidth = width
    ctx.moveTo(x1, y1)
    ctx.lineTo(x2, y2)
    ctx.strokeStyle = fill
    ctx.stroke()

    # 導入數學函式後, 圓周率為 pi
    # deg 為角度轉為徑度的轉換因子
    deg = pi/180.

    # 以下分別為正齒輪繪圖與主 tkinter 畫布繪圖

    # 定義一個繪正齒輪的繪圖函式
    # midx 為齒輪圓心 x 座標
    # midy 為齒輪圓心 y 座標
    # rp 為節圓半徑, n 為齒數
    def gear(midx, midy, rp, n, 顏色):
    # 將角度轉換因子設為全域變數
    global deg
    # 齒輪漸開線分成 15 線段繪製
    imax = 15
    # 在輸入的畫布上繪製直線, 由圓心到節圓 y 軸頂點畫一直線
    create_line(midx, midy, midx, midy-rp)
    # 畫出 rp 圓, 畫圓函式尚未定義
    #create_oval(midx-rp, midy-rp, midx+rp, midy+rp, width=2)
    # a 為模數 (代表公制中齒的大小), 模數為節圓直徑(稱為節徑)除以齒數
    # 模數也就是齒冠大小
    a=2*rp/n
    # d 為齒根大小, 為模數的 1.157 或 1.25倍, 這裡採 1.25 倍
    d=2.5*rp/n
    # ra 為齒輪的外圍半徑
    ra=rp+a
    print("ra:", ra)
    # 畫出 ra 圓, 畫圓函式尚未定義
    #create_oval(midx-ra, midy-ra, midx+ra, midy+ra, width=1)
    # rb 則為齒輪的基圓半徑
    # 基圓為漸開線長齒之基準圓
    rb=rp*cos(20*deg)
    print("rp:", rp)
    print("rb:", rb)
    # 畫出 rb 圓 (基圓), 畫圓函式尚未定義
    #create_oval(midx-rb, midy-rb, midx+rb, midy+rb, width=1)
    # rd 為齒根圓半徑
    rd=rp-d
    # 當 rd 大於 rb 時
    print("rd:", rd)
    # 畫出 rd 圓 (齒根圓), 畫圓函式尚未定義
    #create_oval(midx-rd, midy-rd, midx+rd, midy+rd, width=1)
    # dr 則為基圓到齒頂圓半徑分成 imax 段後的每段半徑增量大小
    # 將圓弧分成 imax 段來繪製漸開線
    dr=(ra-rb)/imax
    # tan(20*deg)-20*deg 為漸開線函數
    sigma=pi/(2*n)+tan(20*deg)-20*deg
    for j in range(n):
        ang=-2.*j*pi/n+sigma
        ang2=2.*j*pi/n+sigma
        lxd=midx+rd*sin(ang2-2.*pi/n)
        lyd=midy-rd*cos(ang2-2.*pi/n)
        #for(i=0;i<=imax;i++):
        for i in range(imax+1):
            r=rb+i*dr
            theta=sqrt((r*r)/(rb*rb)-1.)
            alpha=theta-atan(theta)
            xpt=r*sin(alpha-ang)
            ypt=r*cos(alpha-ang)
            xd=rd*sin(-ang)
            yd=rd*cos(-ang)
            # i=0 時, 繪線起點由齒根圓上的點, 作為起點
            if(i==0):
                last_x = midx+xd
                last_y = midy-yd
            # 由左側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
            create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=顏色)
            # 最後一點, 則為齒頂圓
            if(i==imax):
                lfx=midx+xpt
                lfy=midy-ypt
            last_x = midx+xpt
            last_y = midy-ypt
        # the line from last end of dedendum point to the recent
        # end of dedendum point
        # lxd 為齒根圓上的左側 x 座標, lyd 則為 y 座標
        # 下列為齒根圓上用來近似圓弧的直線
        create_line((lxd),(lyd),(midx+xd),(midy-yd),fill=顏色)
        #for(i=0;i<=imax;i++):
        for i in range(imax+1):
            r=rb+i*dr
            theta=sqrt((r*r)/(rb*rb)-1.)
            alpha=theta-atan(theta)
            xpt=r*sin(ang2-alpha)
            ypt=r*cos(ang2-alpha)
            xd=rd*sin(ang2)
            yd=rd*cos(ang2)
            # i=0 時, 繪線起點由齒根圓上的點, 作為起點
            if(i==0):
                last_x = midx+xd
                last_y = midy-yd
            # 由右側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
            create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=顏色)
            # 最後一點, 則為齒頂圓
            if(i==imax):
                rfx=midx+xpt
                rfy=midy-ypt
            last_x = midx+xpt
            last_y = midy-ypt
        # lfx 為齒頂圓上的左側 x 座標, lfy 則為 y 座標
        # 下列為齒頂圓上用來近似圓弧的直線
        create_line(lfx,lfy,rfx,rfy,fill=顏色)

    gear(400,400,300,41,"blue")
    </script>
    <canvas id="plotarea" width="800" height="800"></canvas>
    </body>
    </html>
    '''

        return outstring
    def gear4(self, m=None, ng1=None, ng2=None, ng3=None, ng4=None, ng5=None, ng6=None, ng7=None, inp2=None):
        outString = ""
        outString +="藍色，齒數1:"+ng1
        outString += "<br />"
        outString +="黑色，齒數2:"+ng2
        outString += "<br />"
        outString +="紅色，齒數3:"+ng3
        outString += "<br />"
        outString +="紫色，齒數4:"+ng4
        outString += "<br />"
        outString +="黃色，齒數5:"+ng5
        outString += "<br />"
        outString +="綠色，齒數6:"+ng6
        outString += "<br />"
        outString +="橘色，齒數7:"+ng7
        outString += "<br />"
        outString +="模數:"+m
        outString += "<br />"
        outString +="壓力角:"+inp2
        outString += "<br />"
        outString += self.menuLink()
        outString += '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">

    <!-- 以下為 canvas 畫圖程式 -->
    <script type="text/python">
    # 從 browser 導入 document
    from browser import document
    from math import *
    # 請注意, 這裡導入位於 Lib/site-packages 目錄下的 spur.py 檔案
    import spur

    # 準備在 id="plotarea" 的 canvas 中繪圖
    canvas = document["plotarea"]
    ctx = canvas.getContext("2d")
    # 以下利用 spur.py 程式進行繪圖, 接下來的協同設計運算必須要配合使用者的需求進行設計運算與繪圖
    # 其中並將工作分配給其他組員建立類似 spur.py 的相關零件繪圖模組
    # midx, midy 為齒輪圓心座標, rp 為節圓半徑, n 為齒數, pa 為壓力角, color 為線的顏色
    # Gear(midx, midy, rp, n=20, pa=20, color="black"):
    # 模數決定齒的尺寸大小, 囓合齒輪組必須有相同的模數與壓力角
    # 壓力角 pa 單位為角度
    pa = '''+str(inp2)+'''

    # m 為模數
    m = '''+str(m)+'''

    # 齒輪齒數
    n_g1 = '''+str(ng1)+'''
    n_g2 = '''+str(ng2)+'''
    n_g3 = '''+str(ng3)+'''
    n_g4 = '''+str(ng4)+'''
    n_g5 = '''+str(ng5)+'''
    n_g6 = '''+str(ng6)+'''
    n_g7 = '''+str(ng7)+'''


    # 計算兩齒輪的節圓半徑
    rp_g1 = m*n_g1/2
    rp_g2 = m*n_g2/2
    rp_g3 = m*n_g3/2
    rp_g4 = m*n_g4/2
    rp_g5 = m*n_g5/2
    rp_g6 = m*n_g6/2
    rp_g7 = m*n_g7/2

    # 繪圖齒輪的圓心座標,假設排列成水平, 表示各齒輪圓心 y 座標相同
    x_g1 = 400
    y_g1 = 400

    x_g2 = x_g1 + rp_g1 + rp_g2
    y_g2 = y_g1

    x_g3 = x_g2 + rp_g2 + rp_g3
    y_g3 = y_g1

    x_g4 = x_g3 + rp_g3 + rp_g4
    y_g4 = y_g1

    x_g5 = x_g4 + rp_g4 + rp_g5 
    y_g5 = y_g1

    x_g6 = x_g5 + rp_g5 + rp_g6 
    y_g6 = y_g1

    x_g7 = x_g6 + rp_g6+ rp_g7
    y_g7 = y_g1
    #齒輪嚙合的旋轉角
    # 將第1齒輪順時鐘轉 90 度
    th1 = pi/2

    # 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    th2 = -pi/2-pi/n_g2

    # 將第3齒輪逆時鐘轉 90 度之後, 再往回轉第2齒輪定位帶動轉角, 然後再逆時鐘多轉一齒, 以便與第2齒輪進行囓合
    # 第1個 -pi/2 為將原先垂直的第3齒輪定位線逆時鐘旋轉 90 度
    # -pi/n_g3 則是第3齒與第2齒定位線重合後, 必須再逆時鐘多轉一齒的轉角, 以便進行囓合
    # (pi+pi/n_g2)*n_g2/n_g3 則是第2齒原定位線為順時鐘轉動 90 度, 
    # pi+pi/n_g2 為第2齒輪從順時鐘轉 90 度之後, 必須配合目前的標記線所作的齒輪 2 轉動角度, 要轉換到齒輪3 的轉動角度
    # 必須乘上兩齒輪齒數的比例, 若齒輪2 大, 則齒輪3 會轉動較快
    # 但是第2齒輪為了與第1齒輪囓合, 已經距離定位線, 多轉了 180 度, 再加上第2齒輪的一齒角度, 因為要帶動第3齒輪定位, 
    # 這個修正角度必須要再配合第2齒與第3齒的轉速比加以轉換成第3齒輪的轉角, 因此乘上 n_g2/n_g3
    th3 = -pi/2-pi/n_g3+(pi+pi/n_g2)*n_g2/n_g3

    th4 = -pi/2-pi/n_g4+(pi+pi/n_g3)*n_g3/n_g4-(pi+pi/n_g2)*n_g2/n_g4
    th5 = -pi/2-pi/n_g5+(pi+pi/n_g4)*n_g4/n_g5-(pi+pi/n_g3)*n_g3/n_g5+(pi+pi/n_g2)*n_g2/n_g5
    th6 = -pi/2-pi/n_g6+(pi+pi/n_g5)*n_g5/n_g6-(pi+pi/n_g4)*n_g4/n_g6+(pi+pi/n_g3)*n_g3/n_g6-(pi+pi/n_g2)*n_g2/n_g6
    th7 = -pi/2-pi/n_g7+(pi+pi/n_g6)*n_g6/n_g7-(pi+pi/n_g5)*n_g5/n_g7+(pi+pi/n_g4)*n_g4/n_g7-(pi+pi/n_g3)*n_g3/n_g7+(pi+pi/n_g2)*n_g2/n_g7



    # 使用 ctx.save() 與 ctx.restore() 以確保各齒輪以相對座標進行旋轉繪圖
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g1,y_g1)
    ctx.rotate(pi/2)
    # put it back
    ctx.translate(-x_g1,-y_g1)
    spur.Spur(ctx).Gear(x_g1,y_g1,rp_g1,n_g1, pa, "blue")
    ctx.restore()


    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g2,y_g2)
    # rotate to engage
    ctx.rotate(th2)
    # put it back
    ctx.translate(-x_g2,-y_g2)
    spur.Spur(ctx).Gear(x_g2,y_g2,rp_g2,n_g2, pa, "black")
    ctx.restore()

    # 假如第3齒也要進行囓合, 又該如何進行繪圖?

    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g3, y_g3)
    # rotate to engage


    ctx.rotate(th3)
    # put it back
    ctx.translate(-x_g3, -y_g3)
    spur.Spur(ctx).Gear(x_g3, y_g3, rp_g3, n_g3, pa, "red")
    ctx.restore()


    # 假如第3齒也要進行囓合, 又該如何進行繪圖?
    # 將第3齒輪逆時鐘轉 90 度之後, 再往回轉第2齒輪定位帶動轉角, 然後再逆時鐘多轉一齒, 以便與第2齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g4, y_g4)
    # rotate to engage
    ctx.rotate(th4)
    # put it back
    ctx.translate(-x_g4, -y_g4)
    spur.Spur(ctx).Gear(x_g4, y_g4, rp_g4, n_g4, pa, "purple")
    ctx.restore()
    ctx.font = "10px Verdana";
    ctx.fillText("組員:29號許家瑋所繪製",x_g4-60, y_g4-10);

    #5
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g5, y_g5)
    # rotate to engage
    ctx.rotate(th5)
    # put it back
    ctx.translate(-x_g5, -y_g5)
    spur.Spur(ctx).Gear(x_g5, y_g5, rp_g5, n_g5, pa, "yellow")
    ctx.restore()

    #6
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g6, y_g6)
    # rotate to engage
    ctx.rotate(th6)
    # put it back
    ctx.translate(-x_g6, -y_g6)
    spur.Spur(ctx).Gear(x_g6, y_g6, rp_g6, n_g6, pa, "green")
    ctx.restore()

    #7
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g7, y_g7)
    # rotate to engage
    ctx.rotate(th7)
    # put it back
    ctx.translate(-x_g7, -y_g7)
    spur.Spur(ctx).Gear(x_g7, y_g7, rp_g7, n_g7, pa, "orange")
    ctx.restore()
    </script>
    <canvas id="plotarea" width="2800" height="1200"></canvas>
    </body>
    </html>
    '''

        return outString
    def index3(self, K=None, N=None, inp2=None):
        # 將標準答案存入 answer session 對應區
        theanswer = random.randint(1, 100)
        thecount = 0
        # 將答案與計算次數變數存進 session 對應變數
        cherrypy.session['answer'] = theanswer
        cherrypy.session['count'] = thecount
        # 印出讓使用者輸入的超文件表單
        outstring = "學號:40223151"
        outstring += "<br />"
        outstring += "姓名:簡正斌"
        outstring += "<br />"
        outstring += "班級:四設二甲"
        outstring += "<br />"
        outstring += '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.0-20150301-090019/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">        
    <form method=\"post\" action=\"mygeartest3\">
        <fieldset>
        <legend>考試協同七個齒輪齒輪參數表單值:</legend>
        齒數1:<br />
        <input type=\"text\" name=\"N\"><br />
        齒數2:<br />
        <input list="ng1" name="ng1">
        <datalist id="ng1">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br />
        齒數3:<br />
        <input list="ng2" name="ng2">
        <datalist id="ng2">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br /><br />
        齒數4: <br />
        <input list="ng3" name="ng3">
        <datalist id="ng3">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br />
        齒數5:<br />
        <input list="ng4" name="ng4">
        <datalist id="ng4">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br />
        齒數6:<br />
        <input list="ng5" name="ng5">
        <datalist id="ng5">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br />
        齒數7:<br />
        <input list="ng6" name="ng6">
        <datalist id="ng6">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br /><br />
        模數:<br />
        <input type=\"text\" name=\"K\"><br />
        壓力角:<br />
        <input type=\"text\" name=\"inp2\"><br />
        <input type=\"submit\" value=\"確定\">
        <input type=\"reset\" value=\"重填\">'''+self.menuLink()+'''
    </form>
    </body>
    </html>
    '''
        outstring +="個人openshift網站"
        outstring +="<font size='4' color='red' >(有影片教學)</font>"
        outstring += "<br />"
        outstring +='''<font size='4' color='yellow' ><a href="http://cd0427-40223151.rhcloud.com/">40223151簡正斌</a> </font>'''
        return outstring
    index3.exposed = True

    #@+node:2015.20150330144929.1713: *3* twoDgear
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def mygeartest3(self, K=None, N=None,ng1=None, ng2=None, ng3=None, ng4=None, ng5=None, ng6=None, inp2=None):
        outString = ""
        outString +="齒數1:"+N
        outString += "<br />"
        outString +="齒數2:"+ng1
        outString += "<br />"
        outString +="齒數3:"+ng2
        outString += "<br />"
        outString +="齒數4:"+ng3
        outString += "<br />"
        outString +="齒數5:"+ng4
        outString += "<br />"
        outString +="齒數6:"+ng5
        outString += "<br />"
        outString +="齒數7:"+ng6
        outString += "<br />"
        outString +="模數:"+K
        outString += "<br />"
        outString +="壓力角:"+inp2
        outString += "<br />"
        outString += self.menuLink()
        outString += '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">

    <!-- 以下為 canvas 畫圖程式 -->
    <script type="text/python">
    # 從 browser 導入 document
    from browser import document
    from math import *
    # 請注意, 這裡導入位於 Lib/site-packages 目錄下的 spur.py 檔案
    import spur

    # 準備在 id="plotarea" 的 canvas 中繪圖
    canvas = document["plotarea"]
    ctx = canvas.getContext("2d")
    # 以下利用 spur.py 程式進行繪圖, 接下來的協同設計運算必須要配合使用者的需求進行設計運算與繪圖
    # 其中並將工作分配給其他組員建立類似 spur.py 的相關零件繪圖模組
    # midx, midy 為齒輪圓心座標, rp 為節圓半徑, n 為齒數, pa 為壓力角, color 為線的顏色
    # Gear(midx, midy, rp, n=20, pa=20, color="black"):
    # 模數決定齒的尺寸大小, 囓合齒輪組必須有相同的模數與壓力角
    # 壓力角 pa 單位為角度
    pa = '''+str(inp2)+'''
    # m 為模數
    m = '''+str(K)+'''
    # 第1齒輪齒數
    n_g1 = '''+str(N)+'''
    # 第2齒輪齒數
    n_g2 = '''+str(ng1)+'''
    n_g3 = '''+str(ng2)+'''
    n_g4 = '''+str(ng3)+'''
    n_g5 = '''+str(ng4)+'''
    n_g6 = '''+str(ng5)+'''
    n_g7 = '''+str(ng6)+'''
    # 計算兩齒輪的節圓半徑
    rp_g1 = m*n_g1/2
    rp_g2 = m*n_g2/2
    rp_g3 = m*n_g3/2
    rp_g4 = m*n_g4/2
    rp_g5 = m*n_g5/2
    rp_g6 = m*n_g6/2
    rp_g7 = m*n_g7/2
 #齒輪嚙合的旋轉角
# 將第1齒輪順時鐘轉 90 度
    th1 = pi/2

    # 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    th2 = -pi/2-pi/n_g2

    # 將第3齒輪逆時鐘轉 90 度之後, 再往回轉第2齒輪定位帶動轉角, 然後再逆時鐘多轉一齒, 以便與第2齒輪進行囓合
    # 第1個 -pi/2 為將原先垂直的第3齒輪定位線逆時鐘旋轉 90 度
    # -pi/n_g3 則是第3齒與第2齒定位線重合後, 必須再逆時鐘多轉一齒的轉角, 以便進行囓合
    # (pi+pi/n_g2)*n_g2/n_g3 則是第2齒原定位線為順時鐘轉動 90 度, 
    # pi+pi/n_g2 為第2齒輪從順時鐘轉 90 度之後, 必須配合目前的標記線所作的齒輪 2 轉動角度, 要轉換到齒輪3 的轉動角度
    # 必須乘上兩齒輪齒數的比例, 若齒輪2 大, 則齒輪3 會轉動較快
    # 但是第2齒輪為了與第1齒輪囓合, 已經距離定位線, 多轉了 180 度, 再加上第2齒輪的一齒角度, 因為要帶動第3齒輪定位, 
    # 這個修正角度必須要再配合第2齒與第3齒的轉速比加以轉換成第3齒輪的轉角, 因此乘上 n_g2/n_g3
    th3 = -pi/2-pi/n_g3+(pi+pi/n_g2)*n_g2/n_g3

    th4 = -pi/2-pi/n_g4+(pi+pi/n_g3)*n_g3/n_g4-(pi+pi/n_g2)*n_g2/n_g4
    th5 = -pi/2-pi/n_g5+(pi+pi/n_g4)*n_g4/n_g5-(pi+pi/n_g3)*n_g3/n_g5+(pi+pi/n_g2)*n_g2/n_g5
    th6 = -pi/2-pi/n_g6+(pi+pi/n_g5)*n_g5/n_g6-(pi+pi/n_g4)*n_g4/n_g6+(pi+pi/n_g3)*n_g3/n_g6-(pi+pi/n_g2)*n_g2/n_g6
    th7 = -pi/2-pi/n_g7+(pi+pi/n_g6)*n_g6/n_g7-(pi+pi/n_g5)*n_g5/n_g7+(pi+pi/n_g4)*n_g4/n_g7-(pi+pi/n_g3)*n_g3/n_g7+(pi+pi/n_g2)*n_g2/n_g7


    # 將第1齒輪順時鐘轉 90 度
    # 使用 ctx.save() 與 ctx.restore() 以確保各齒輪以相對座標進行旋轉繪圖
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400,400)
    # rotate to engage
    ctx.rotate( th1)
    # put it back
    ctx.translate(-400,-400)
    spur.Spur(ctx).Gear(400,400,rp_g1,n_g1, pa, "blue")
    ctx.restore()
    ctx.font = "10px Verdana";
    ctx.fillText("組員:24號袁丞宗所繪製",400-60, 400-10);

    # 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400+rp_g1+rp_g2,400)
    # rotate to engage
    ctx.rotate( th2)
    # put it back
    ctx.translate(-(400+rp_g1+rp_g2),-400)
    spur.Spur(ctx).Gear(400+rp_g1+rp_g2,400,rp_g2,n_g2, pa, "black")
    ctx.restore()

    # 將第3齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400+rp_g1+2*rp_g2+rp_g3,400)
    # rotate to engage
    ctx.rotate( th3)
    # put it back
    ctx.translate(-(400+rp_g1+2*rp_g2+rp_g3),-400)
    spur.Spur(ctx).Gear(400+rp_g1+2*rp_g2+rp_g3,400,rp_g3,n_g3, pa, "red")
    ctx.restore()

    # 將第4齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400+rp_g1+2*rp_g2+2*rp_g3+rp_g4,400)
    # rotate to engage
    ctx.rotate( th4)
    # put it back
    ctx.translate(-(400+rp_g1+2*rp_g2+2*rp_g3+rp_g4),-400)
    spur.Spur(ctx).Gear(400+rp_g1+2*rp_g2+2*rp_g3+rp_g4,400,rp_g4,n_g4, pa, "black")
    ctx.restore()

    # 將第5齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+rp_g5,400)
    # rotate to engage
    ctx.rotate( th5)
    # put it back
    ctx.translate(-(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+rp_g5),-400)
    spur.Spur(ctx).Gear(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+rp_g5,400,rp_g5,n_g5 ,pa, "green")
    ctx.restore()

    # 將第6齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+2*rp_g5+rp_g6,400)
    # rotate to engage
    ctx.rotate( th6)
    # put it back
    ctx.translate(-(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+2*rp_g5+rp_g6),-400)
    spur.Spur(ctx).Gear(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+2*rp_g5+rp_g6,400,rp_g6,n_g6 ,pa, "yellow")
    ctx.restore()

    # 將第7齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+2*rp_g5+2*rp_g6+rp_g7,400)
    # rotate to engage
    ctx.rotate( th7)
    # put it back
    ctx.translate(-(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+2*rp_g5+2*rp_g6+rp_g7),-400)
    spur.Spur(ctx).Gear(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+2*rp_g5+2*rp_g6+rp_g7,400,rp_g7,n_g7 ,pa, "pink")
    ctx.restore()
    # 假如第3齒也要進行囓合, 又該如何進行繪圖?
    #spur.Spur(ctx).Gear(400,400,100,12, pa, "red")

    </script>
    <canvas id="plotarea" width="3600" height="3600"></canvas>
    </body>
    </html>
    '''

        return outString
    mygeartest3.exposed = True

    #@-others
    def index2(self, K=None, N=None, inp2=None):
        # 將標準答案存入 answer session 對應區
        theanswer = random.randint(1, 100)
        thecount = 0
        # 將答案與計算次數變數存進 session 對應變數
        cherrypy.session['answer'] = theanswer
        cherrypy.session['count'] = thecount
        # 印出讓使用者輸入的超文件表單
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.0-20150301-090019/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">
    <form method=\"post\" action=\"doAct\">
        <fieldset>
        <legend>功課齒輪參數表單:</legend>
        齒數:<br />
        <input type=\"text\" name=\"N\"><br />

        </select>
        模數:<br />
        <input type=\"text\" name=\"K\"><br />
        壓力角(>33時會有錯誤):<br />
        <input type=\"text\" name=\"inp2\"><br />
        <input type=\"submit\" value=\"確定\">
        <input type=\"reset\" value=\"重填\">
        <a href="gear">3D齒輪模式</a>
    </form>
        
    <form method=\"post\" action=\"mygeartest2\">
        <fieldset>
        <legend>協同考試七個齒輪契合齒輪參數表單值:</legend>
        齒數1:<br />
        <input type=\"text\" name=\"ng1\"><br />
        齒數2:<br />
        <input type=\"text\" name=\"ng2\"><br />
        齒數3:<br />
        <input type=\"text\" name=\"ng3\"><br />
        齒數4:<br />
        <input type=\"text\" name=\"ng4\"><br />
        齒數5:<br />
        <input type=\"text\" name=\"ng5\"><br />
        齒數6:<br />
        <input type=\"text\" name=\"ng6\"><br />
        齒數7:<br />
        <input type=\"text\" name=\"ng7\"><br />
        </select>
        模數:<br />
        <input type=\"text\" name=\"m\"><br />
        壓力角(>33時會有錯誤):<br />
        <input type=\"text\" name=\"inp2\"><br />
        <input type=\"submit\" value=\"確定\">
        <input type=\"reset\" value=\"重填\">
    </form>
    3D齒輪模式操作圖示<img src="https://copy.com/LEfCvgTRr6ptU2Jv"><br />
    <img src="https://copy.com/ZpzLF8IqeJRN0D3O"><br />
    <img src="https://copy.com/thumbs/cda/3Dgear3.png?size=1024&revision=80"><br />
    <hr>
    <!-- 以下在網頁內嵌 Brython 程式 -->
    <script type="text/python">
    from browser import document, alert

    def echo(ev):
        alert(document["zone"].value)

    # 將文件中名稱為 mybutton 的物件, 透過 click 事件與 echo 函式 bind 在一起
    document['mybutton'].bind('click',echo)
    </script>

    <!-- 以下為 canvas 畫圖程式 -->
<script type="text/python">
# 從 browser 導入 document
from browser import document
from math import *

# 準備在 id="plotarea" 的 canvas 中繪圖
canvas = document["plotarea"]
ctx = canvas.getContext("2d")

def create_line(x1, y1, x2, y2, width=3, fill="red"):
    ctx.beginPath()
    ctx.lineWidth = width
    ctx.moveTo(x1, y1)
    ctx.lineTo(x2, y2)
    ctx.strokeStyle = fill
    ctx.stroke()

# 導入數學函式後, 圓周率為 pi
# deg 為角度轉為徑度的轉換因子
deg = pi/180.
#
# 以下分別為正齒輪繪圖與主 tkinter 畫布繪圖
#
# 定義一個繪正齒輪的繪圖函式
# midx 為齒輪圓心 x 座標
# midy 為齒輪圓心 y 座標
# rp 為節圓半徑, n 為齒數
def gear(midx, midy, rp, n, 顏色):
    # 將角度轉換因子設為全域變數
    global deg
    # 齒輪漸開線分成 15 線段繪製
    imax = 15
    # 在輸入的畫布上繪製直線, 由圓心到節圓 y 軸頂點畫一直線
    create_line(midx, midy, midx, midy-rp)
    # 畫出 rp 圓, 畫圓函式尚未定義
    #create_oval(midx-rp, midy-rp, midx+rp, midy+rp, width=2)
    # a 為模數 (代表公制中齒的大小), 模數為節圓直徑(稱為節徑)除以齒數
    # 模數也就是齒冠大小
    a=2*rp/n
    # d 為齒根大小, 為模數的 1.157 或 1.25倍, 這裡採 1.25 倍
    d=2.5*rp/n
    # ra 為齒輪的外圍半徑
    ra=rp+a
    print("ra:", ra)
    # 畫出 ra 圓, 畫圓函式尚未定義
    #create_oval(midx-ra, midy-ra, midx+ra, midy+ra, width=1)
    # rb 則為齒輪的基圓半徑
    # 基圓為漸開線長齒之基準圓
    rb=rp*cos(20*deg)
    print("rp:", rp)
    print("rb:", rb)
    # 畫出 rb 圓 (基圓), 畫圓函式尚未定義
    #create_oval(midx-rb, midy-rb, midx+rb, midy+rb, width=1)
    # rd 為齒根圓半徑
    rd=rp-d
    # 當 rd 大於 rb 時
    print("rd:", rd)
    # 畫出 rd 圓 (齒根圓), 畫圓函式尚未定義
    #create_oval(midx-rd, midy-rd, midx+rd, midy+rd, width=1)
    # dr 則為基圓到齒頂圓半徑分成 imax 段後的每段半徑增量大小
    # 將圓弧分成 imax 段來繪製漸開線
    dr=(ra-rb)/imax
    # tan(20*deg)-20*deg 為漸開線函數
    sigma=pi/(2*n)+tan(20*deg)-20*deg
    for j in range(n):
        ang=-2.*j*pi/n+sigma
        ang2=2.*j*pi/n+sigma
        lxd=midx+rd*sin(ang2-2.*pi/n)
        lyd=midy-rd*cos(ang2-2.*pi/n)
        #for(i=0;i<=imax;i++):
        for i in range(imax+1):
            r=rb+i*dr
            theta=sqrt((r*r)/(rb*rb)-1.)
            alpha=theta-atan(theta)
            xpt=r*sin(alpha-ang)
            ypt=r*cos(alpha-ang)
            xd=rd*sin(-ang)
            yd=rd*cos(-ang)
            # i=0 時, 繪線起點由齒根圓上的點, 作為起點
            if(i==0):
                last_x = midx+xd
                last_y = midy-yd
            # 由左側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
            create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=顏色)
            # 最後一點, 則為齒頂圓
            if(i==imax):
                lfx=midx+xpt
                lfy=midy-ypt
            last_x = midx+xpt
            last_y = midy-ypt
        # the line from last end of dedendum point to the recent
        # end of dedendum point
        # lxd 為齒根圓上的左側 x 座標, lyd 則為 y 座標
        # 下列為齒根圓上用來近似圓弧的直線
        create_line((lxd),(lyd),(midx+xd),(midy-yd),fill=顏色)
        #for(i=0;i<=imax;i++):
        for i in range(imax+1):
            r=rb+i*dr
            theta=sqrt((r*r)/(rb*rb)-1.)
            alpha=theta-atan(theta)
            xpt=r*sin(ang2-alpha)
            ypt=r*cos(ang2-alpha)
            xd=rd*sin(ang2)
            yd=rd*cos(ang2)
            # i=0 時, 繪線起點由齒根圓上的點, 作為起點
            if(i==0):
                last_x = midx+xd
                last_y = midy-yd
            # 由右側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
            create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=顏色)
            # 最後一點, 則為齒頂圓
            if(i==imax):
                rfx=midx+xpt
                rfy=midy-ypt
            last_x = midx+xpt
            last_y = midy-ypt
        # lfx 為齒頂圓上的左側 x 座標, lfy 則為 y 座標
        # 下列為齒頂圓上用來近似圓弧的直線
        create_line(lfx,lfy,rfx,rfy,fill=顏色)

gear(400,400,300,41,"blue")
</script>
<canvas id="plotarea" width="800" height="800"></canvas>
</body>
</html>
    '''

        return outstring
    index2.exposed = True
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def mygeartest2(self, m=None, ng1=None, ng2=None, ng3=None, ng4=None, ng5=None, ng6=None, ng7=None, inp2=None):
        outString = ""
        outString +="藍色，24號丞宗所繪製，齒數1:"+ng1
        outString += "<br />"
        outString +="黑色，45號兆銓所繪製，齒數2:"+ng2
        outString += "<br />"
        outString +="紅色，10號常浩所繪製，齒數3:"+ng3
        outString += "<br />"
        outString +="紫色，29號家偉所繪製，齒數4:"+ng4
        outString += "<br />"
        outString +="黃色，49號涵餘所繪製，齒數5:"+ng5
        outString += "<br />"
        outString +="綠色，50號俊宇所繪製，齒數6:"+ng6
        outString += "<br />"
        outString +="橘色，51號正斌所繪製，齒數7:"+ng7
        outString += "<br />"
        outString +="模數:"+m
        outString += "<br />"
        outString +="壓力角:"+inp2
        outString += "<br />"
        outString += self.menuLink()
        outString += '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">

    <!-- 以下為 canvas 畫圖程式 -->
    <script type="text/python">
    # 從 browser 導入 document
    from browser import document
    from math import *
    # 請注意, 這裡導入位於 Lib/site-packages 目錄下的 spur.py 檔案
    import spur

    # 準備在 id="plotarea" 的 canvas 中繪圖
    canvas = document["plotarea"]
    ctx = canvas.getContext("2d")
    # 以下利用 spur.py 程式進行繪圖, 接下來的協同設計運算必須要配合使用者的需求進行設計運算與繪圖
    # 其中並將工作分配給其他組員建立類似 spur.py 的相關零件繪圖模組
    # midx, midy 為齒輪圓心座標, rp 為節圓半徑, n 為齒數, pa 為壓力角, color 為線的顏色
    # Gear(midx, midy, rp, n=20, pa=20, color="black"):
    # 模數決定齒的尺寸大小, 囓合齒輪組必須有相同的模數與壓力角
    # 壓力角 pa 單位為角度
    pa = '''+str(inp2)+'''

    # m 為模數
    m = '''+str(m)+'''

    # 齒輪齒數
    n_g1 = '''+str(ng1)+'''
    n_g2 = '''+str(ng2)+'''
    n_g3 = '''+str(ng3)+'''
    n_g4 = '''+str(ng4)+'''
    n_g5 = '''+str(ng5)+'''
    n_g6 = '''+str(ng6)+'''
    n_g7 = '''+str(ng7)+'''


    # 計算兩齒輪的節圓半徑
    rp_g1 = m*n_g1/2
    rp_g2 = m*n_g2/2
    rp_g3 = m*n_g3/2
    rp_g4 = m*n_g4/2
    rp_g5 = m*n_g5/2
    rp_g6 = m*n_g6/2
    rp_g7 = m*n_g7/2

    # 繪圖齒輪的圓心座標,假設排列成水平, 表示各齒輪圓心 y 座標相同
    x_g1 = 400
    y_g1 = 400

    x_g2 = x_g1 + rp_g1 + rp_g2
    y_g2 = y_g1

    x_g3 = x_g2 + rp_g2 + rp_g3
    y_g3 = y_g1

    x_g4 = x_g3 + rp_g3 + rp_g4
    y_g4 = y_g1

    x_g5 = x_g4 + rp_g4 + rp_g5 
    y_g5 = y_g1

    x_g6 = x_g5 + rp_g5 + rp_g6 
    y_g6 = y_g1

    x_g7 = x_g6 + rp_g6+ rp_g7
    y_g7 = y_g1
    #齒輪嚙合的旋轉角
    # 將第1齒輪順時鐘轉 90 度
    th1 = pi/2

    # 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    th2 = -pi/2-pi/n_g2

    # 將第3齒輪逆時鐘轉 90 度之後, 再往回轉第2齒輪定位帶動轉角, 然後再逆時鐘多轉一齒, 以便與第2齒輪進行囓合
    # 第1個 -pi/2 為將原先垂直的第3齒輪定位線逆時鐘旋轉 90 度
    # -pi/n_g3 則是第3齒與第2齒定位線重合後, 必須再逆時鐘多轉一齒的轉角, 以便進行囓合
    # (pi+pi/n_g2)*n_g2/n_g3 則是第2齒原定位線為順時鐘轉動 90 度, 
    # pi+pi/n_g2 為第2齒輪從順時鐘轉 90 度之後, 必須配合目前的標記線所作的齒輪 2 轉動角度, 要轉換到齒輪3 的轉動角度
    # 必須乘上兩齒輪齒數的比例, 若齒輪2 大, 則齒輪3 會轉動較快
    # 但是第2齒輪為了與第1齒輪囓合, 已經距離定位線, 多轉了 180 度, 再加上第2齒輪的一齒角度, 因為要帶動第3齒輪定位, 
    # 這個修正角度必須要再配合第2齒與第3齒的轉速比加以轉換成第3齒輪的轉角, 因此乘上 n_g2/n_g3
    th3 = -pi/2-pi/n_g3+(pi+pi/n_g2)*n_g2/n_g3

    th4 = -pi/2-pi/n_g4+(pi+pi/n_g3)*n_g3/n_g4-(pi+pi/n_g2)*n_g2/n_g4
    th5 = -pi/2-pi/n_g5+(pi+pi/n_g4)*n_g4/n_g5-(pi+pi/n_g3)*n_g3/n_g5+(pi+pi/n_g2)*n_g2/n_g5
    th6 = -pi/2-pi/n_g6+(pi+pi/n_g5)*n_g5/n_g6-(pi+pi/n_g4)*n_g4/n_g6+(pi+pi/n_g3)*n_g3/n_g6-(pi+pi/n_g2)*n_g2/n_g6
    th7 = -pi/2-pi/n_g7+(pi+pi/n_g6)*n_g6/n_g7-(pi+pi/n_g5)*n_g5/n_g7+(pi+pi/n_g4)*n_g4/n_g7-(pi+pi/n_g3)*n_g3/n_g7+(pi+pi/n_g2)*n_g2/n_g7



    # 使用 ctx.save() 與 ctx.restore() 以確保各齒輪以相對座標進行旋轉繪圖
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g1,y_g1)
    ctx.rotate(pi/2)
    # put it back
    ctx.translate(-x_g1,-y_g1)
    spur.Spur(ctx).Gear(x_g1,y_g1,rp_g1,n_g1, pa, "blue")
    ctx.restore()
    ctx.font = "10px Verdana";
    ctx.fillText("組員:24號袁丞宗所繪製",x_g1-60, y_g1-10);

    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g2,y_g2)
    # rotate to engage
    ctx.rotate(th2)
    # put it back
    ctx.translate(-x_g2,-y_g2)
    spur.Spur(ctx).Gear(x_g2,y_g2,rp_g2,n_g2, pa, "black")
    ctx.restore()

    # 假如第3齒也要進行囓合, 又該如何進行繪圖?

    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g3, y_g3)
    # rotate to engage


    ctx.rotate(th3)
    # put it back
    ctx.translate(-x_g3, -y_g3)
    spur.Spur(ctx).Gear(x_g3, y_g3, rp_g3, n_g3, pa, "red")
    ctx.restore()

    # 假如第3齒也要進行囓合, 又該如何進行繪圖?
    # 將第3齒輪逆時鐘轉 90 度之後, 再往回轉第2齒輪定位帶動轉角, 然後再逆時鐘多轉一齒, 以便與第2齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g4, y_g4)
    # rotate to engage
    ctx.rotate(th4)
    # put it back
    ctx.translate(-x_g4, -y_g4)
    spur.Spur(ctx).Gear(x_g4, y_g4, rp_g4, n_g4, pa, "purple")
    ctx.restore()

    #5
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g5, y_g5)
    # rotate to engage
    ctx.rotate(th5)
    # put it back
    ctx.translate(-x_g5, -y_g5)
    spur.Spur(ctx).Gear(x_g5, y_g5, rp_g5, n_g5, pa, "yellow")
    ctx.restore()

    #6
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g6, y_g6)
    # rotate to engage
    ctx.rotate(th6)
    # put it back
    ctx.translate(-x_g6, -y_g6)
    spur.Spur(ctx).Gear(x_g6, y_g6, rp_g6, n_g6, pa, "green")
    ctx.restore()

    #7
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g7, y_g7)
    # rotate to engage
    ctx.rotate(th7)
    # put it back
    ctx.translate(-x_g7, -y_g7)
    spur.Spur(ctx).Gear(x_g7, y_g7, rp_g7, n_g7, pa, "orange")
    ctx.restore()
    </script>
    <canvas id="plotarea" width="2800" height="1200"></canvas>
    </body>
    </html>
    '''

        return outString
    mygeartest2.exposed = True

    @cherrypy.expose
    def doAct(self, K=None, N=None, inp2=None):
        inp3=int(N)*int(K)/2
        #inp 變數即為表單值, 其格式為字串
        outString = ""
        outString +="齒數:"+N
        outString += "<br />"
        outString +="模數:"+K
        outString += "<br />"
        outString +="壓力角:"+inp2
        outString += "<br />"
        outString += self.menuLink()
        outString += '''

    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.0-20150301-090019/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">
    <hr>
    <!-- 以下為 canvas 畫圖程式 -->
<script type="text/python">
# 從 browser 導入 document
from browser import document
from math import *

# 準備在 id="plotarea" 的 canvas 中繪圖
canvas = document["plotarea"]
ctx = canvas.getContext("2d")

def create_line(x1, y1, x2, y2, width=3, fill="red"):
    ctx.beginPath()
    ctx.lineWidth = width
    ctx.moveTo(x1, y1)
    ctx.lineTo(x2, y2)
    ctx.strokeStyle = fill
    ctx.stroke()

# 導入數學函式後, 圓周率為 pi
# deg 為角度轉為徑度的轉換因子
deg = pi/180.
#
# 以下分別為正齒輪繪圖與主 tkinter 畫布繪圖
#
# 定義一個繪正齒輪的繪圖函式
# midx 為齒輪圓心 x 座標
# midy 為齒輪圓心 y 座標
# rp 為節圓半徑, n 為齒數
def gear(midx1, midy, j, n, 顏色):
    # 將角度轉換因子設為全域變數
    global deg
    # 齒輪漸開線分成 15 線段繪製
    imax = 15
    # 在輸入的畫布上繪製直線, 由圓心到節圓 y 軸頂點畫一直線
    rp=j*n/2
    if (midx1>0):
        midx=midx1
    else:
        midx=400+(rp+6)*2
    create_line(midx, midy, midx, midy-rp)
    # 畫出 rp 圓, 畫圓函式尚未定義
    #create_oval(midx-rp, midy-rp, midx+rp, midy+rp, width=2)
    # a 為模數 (代表公制中齒的大小), 模數為節圓直徑(稱為節徑)除以齒數
    # 模數也就是齒冠大小
    a=2*rp/n
    # d 為齒根大小, 為模數的 1.157 或 1.25倍, 這裡採 1.25 倍
    d=2.5*rp/n
    # ra 為齒輪的外圍半徑
    ra=rp+a
    print("ra:", ra)
    # 畫出 ra 圓, 畫圓函式尚未定義
    #create_oval(midx-ra, midy-ra, midx+ra, midy+ra, width=1)
    # rb 則為齒輪的基圓半徑
    # 基圓為漸開線長齒之基準圓
    rb=rp*cos(20*deg)
    print("rp:", rp)
    print("rb:", rb)
    # 畫出 rb 圓 (基圓), 畫圓函式尚未定義
    #create_oval(midx-rb, midy-rb, midx+rb, midy+rb, width=1)
    # rd 為齒根圓半徑
    rd=rp-d
    # 當 rd 大於 rb 時
    print("rd:", rd)
    # 畫出 rd 圓 (齒根圓), 畫圓函式尚未定義
    #create_oval(midx-rd, midy-rd, midx+rd, midy+rd, width=1)
    # dr 則為基圓到齒頂圓半徑分成 imax 段後的每段半徑增量大小
    # 將圓弧分成 imax 段來繪製漸開線
    dr=(ra-rb)/imax
    # tan(20*deg)-20*deg 為漸開線函數
    sigma=pi/(2*n)+tan('''+(inp2)+'''*deg)-'''+(inp2)+'''*deg
    for j in range(n):
        ang=-2.*j*pi/n+sigma
        ang2=2.*j*pi/n+sigma
        lxd=midx+rd*sin(ang2-2.*pi/n)
        lyd=midy-rd*cos(ang2-2.*pi/n)
        #for(i=0;i<=imax;i++):
        for i in range(imax+1):
            r=rb+i*dr
            theta=sqrt((r*r)/(rb*rb)-1.)
            alpha=theta-atan(theta)
            xpt=r*sin(alpha-ang)
            ypt=r*cos(alpha-ang)
            xd=rd*sin(-ang)
            yd=rd*cos(-ang)
            # i=0 時, 繪線起點由齒根圓上的點, 作為起點
            if(i==0):
                last_x = midx+xd
                last_y = midy-yd
            # 由左側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
            create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=顏色)
            # 最後一點, 則為齒頂圓
            if(i==imax):
                lfx=midx+xpt
                lfy=midy-ypt
            last_x = midx+xpt
            last_y = midy-ypt
        # the line from last end of dedendum point to the recent
        # end of dedendum point
        # lxd 為齒根圓上的左側 x 座標, lyd 則為 y 座標
        # 下列為齒根圓上用來近似圓弧的直線
        create_line((lxd),(lyd),(midx+xd),(midy-yd),fill=顏色)
        #for(i=0;i<=imax;i++):
        for i in range(imax+1):
            r=rb+i*dr
            theta=sqrt((r*r)/(rb*rb)-1.)
            alpha=theta-atan(theta)
            xpt=r*sin(ang2-alpha)
            ypt=r*cos(ang2-alpha)
            xd=rd*sin(ang2)
            yd=rd*cos(ang2)
            # i=0 時, 繪線起點由齒根圓上的點, 作為起點
            if(i==0):
                last_x = midx+xd
                last_y = midy-yd
            # 由右側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
            create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=顏色)
            # 最後一點, 則為齒頂圓
            if(i==imax):
                rfx=midx+xpt
                rfy=midy-ypt
            last_x = midx+xpt
            last_y = midy-ypt
        # lfx 為齒頂圓上的左側 x 座標, lfy 則為 y 座標
        # 下列為齒頂圓上用來近似圓弧的直線
        create_line(lfx,lfy,rfx,rfy,fill=顏色)

gear(400,400,'''+str(K)+''','''+str(N)+''',"blue")
gear(0,400,'''+str(K)+''','''+str(N)+'''-2,"read")
</script>
<canvas id="plotarea" width="1000" height="1000"></canvas>
</body>
</html>
    '''

        return outString
    doAct.exposed = True
    def guessform(self):
        # 印出讓使用者輸入的超文件表單
        outstring = str(cherrypy.session.get('answer')) + "/" + str(cherrypy.session.get('count')) + '''<form method=POST action=doCheck>
    請輸入您所猜的整數:<input type=text name=guess><br />
    <input type=submit value=send>
    </form>'''
        return outstring0
    def twoDgear(self, N=20, M=5, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.0-20150301-090019/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">
        
    <form method=POST action=do2Dgear>
    齒數:<input type=text name=N><br />
    模數:<input type=text name=M><br />
    壓力角:<input type=text name=P><br />
    <input type=submit value=send>
    </form>
    </body>
    </html>
    '''

        return outstring
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def do2Dgear(self, N=20, M=5, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.0-20150301-090019/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">
    <!-- 以下為 canvas 畫圖程式 -->
    <script type="text/python">
    # 從 browser 導入 document
    from browser import document
    import math

    # 畫布指定在名稱為 plotarea 的 canvas 上
    canvas = document["plotarea"]
    ctx = canvas.getContext("2d")

    # 用紅色畫一條直線
    ctx.beginPath()
    ctx.lineWidth = 3
    '''
        outstring += '''
    ctx.moveTo('''+str(N)+","+str(M)+")"
        outstring += '''
    ctx.lineTo(0, 500)
    ctx.strokeStyle = "red"
    ctx.stroke()

    # 用藍色再畫一條直線
    ctx.beginPath()
    ctx.lineWidth = 3
    ctx.moveTo(0, 0)
    ctx.lineTo(500, 0)
    ctx.strokeStyle = "blue"
    ctx.stroke()

    # 用綠色再畫一條直線
    ctx.beginPath()
    ctx.lineWidth = 3
    ctx.moveTo(0, 0)
    ctx.lineTo(500, 500)
    ctx.strokeStyle = "green"
    ctx.stroke()

    # 用黑色畫一個圓
    ctx.beginPath()
    ctx.lineWidth = 3
    ctx.strokeStyle = "black"
    ctx.arc(250,250,50,0,2*math.pi)
    ctx.stroke()
    </script>
    <canvas id="plotarea" width="800" height="600"></canvas>
    </body>
    </html>
    '''

        return outstring
    def default(self):
        sys.exit()
    default.exposed = True
    def menuLink(self):
        return '''
        <br />
        <a href=\"index\">首頁</a>|
        <br />
        '''
################# (4) 程式啟動區
# 配合程式檔案所在目錄設定靜態目錄或靜態檔案
application_conf = {'/static':{
        'tools.staticdir.on': True,
        # 程式執行目錄下, 必須自行建立 static 目錄
        'tools.staticdir.dir': _curdir+"/static"},
        '/downloads':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/downloads"},
        '/images':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/images"}
    }
root = Hello()
root.gear = gear.Gear()
root.legoman = legoman.MAN()
cherrypy.server.socket_port = 8082
cherrypy.server.socket_host = '127.0.0.1'
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示在 OpenSfhit 執行
    application = cherrypy.Application(root, config=application_conf)
else:
    # 表示在近端執行
    cherrypy.quickstart(root, config=application_conf)
