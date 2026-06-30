# ==========================================
# 小遊戲一：逃出迷霧 相關邏輯與畫面
# ==========================================

# 初始化變數
default minigame_timer_duration = 60
default minigame_timer_value = 60
default minigame_timer_running = False

# 遊戲一說明與計時器畫面
screen minigame_1_screen():
    modal True
    
    # 半透明黑色背景蓋住後方
    add Solid("#000000aa")
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 680
        padding (40, 40)
        
        vbox:
            spacing 15
            xalign 0.5
            
            # 遊戲標題
            text "遊戲一 逃出迷霧 (平均乘 0.8)" size 36 color "#FFD700" xalign 0.5 bold True
            
            # 引言
            text "「大霧會放大水手的貪婪與迷惘，唯有摒除兩成的幻覺，才能看清真實的航向。」" size 22 italic True color "#aed8f2" xalign 0.5
            
            # 規則說明框
            frame:
                background Solid("#1c2230cc")
                padding (25, 25)
                xsize 820
                xalign 0.5
                
                vbox:
                    spacing 12
                    text "【遊戲規則】" size 26 bold True color "#4ECDC4"
                    text "1. 每個小隊在小白板上寫下一個 1~100 的整數，代表預測的航行距離。" size 20 color "#ffffff"
                    text "2. 所有小隊數值的「平均數」將作為總體預測值。" size 20 color "#ffffff"
                    text "3. 由於大霧會放大幻覺，反推得到的真實航行距離為：總體預測 × 0.8。" size 20 color "#fcd34d" bold True
                    text "4. 與真實距離最近的前三名小隊，將分別獲得 3 分、2 分、1 分。" size 20 color "#ffffff"
            
            null height 5
            
            # 計時器展示與控制區 (縮小元件)
            vbox:
                spacing 8
                xalign 0.5
                
                # 倒數計時顯示 (從 48 縮小至 32)
                text "[minigame_timer_value] 秒" size 32 color "#ff5555" xalign 0.5 bold True
                
                # 時間進度條 (縮短且變細)
                bar:
                    value minigame_timer_value
                    range minigame_timer_duration
                    xalign 0.5
                    xsize 350
                    ysize 8
                
                # 設定時間面板 (字型縮小至 14)
                if not minigame_timer_running:
                    hbox:
                        spacing 10
                        xalign 0.5
                        yalign 0.5
                        text "設定倒數時間：" size 14 color "#cccccc" yalign 0.5
                        
                        textbutton "30 秒" action [SetVariable("minigame_timer_duration", 30), SetVariable("minigame_timer_value", 30)] text_size 14
                        textbutton "60 秒" action [SetVariable("minigame_timer_duration", 60), SetVariable("minigame_timer_value", 60)] text_size 14
                        textbutton "90 秒" action [SetVariable("minigame_timer_duration", 90), SetVariable("minigame_timer_value", 90)] text_size 14
                        textbutton "120 秒" action [SetVariable("minigame_timer_duration", 120), SetVariable("minigame_timer_value", 120)] text_size 14
                        
                        hbox:
                            spacing 3
                            textbutton "-10" action [SetVariable("minigame_timer_duration", max(10, minigame_timer_duration - 10)), SetVariable("minigame_timer_value", max(10, minigame_timer_value - 10))] text_size 14
                            textbutton "+10" action [SetVariable("minigame_timer_duration", minigame_timer_duration + 10), SetVariable("minigame_timer_value", minigame_timer_value + 10)] text_size 14
                
                # 計時器控制按鈕 (字型縮小至 16)
                hbox:
                    spacing 20
                    xalign 0.5
                    
                    if not minigame_timer_running:
                        textbutton "開始計時" action SetVariable("minigame_timer_running", True) text_color "#4ECDC4" text_size 16
                    else:
                        textbutton "暫停計時" action SetVariable("minigame_timer_running", False) text_color "#ffb6b6" text_size 16
                        
                    textbutton "重設時間" action [SetVariable("minigame_timer_running", False), SetVariable("minigame_timer_value", minigame_timer_duration)] text_size 16
            
            null height 10
            
            # 開始與下一步 (字型縮小至 18)
            textbutton "關閉說明，進入登島劇情" action Return() xalign 0.5 text_size 18 text_color "#ffffff" text_hover_color "#FFD700"

    # 計時器觸發器邏輯
    if minigame_timer_running and minigame_timer_value > 0:
        timer 1.0 action SetVariable("minigame_timer_value", minigame_timer_value - 1) repeat True
    elif minigame_timer_running and minigame_timer_value <= 0:
        timer 0.1 action [SetVariable("minigame_timer_running", False), Notify("時間到！時間已結束！")]

# ==========================================
# 小遊戲一進入點 Label
# ==========================================
label minigame_1:
    # 初始化計時器數值，防止繼承舊資料
    $ minigame_timer_duration = 60
    $ minigame_timer_value = 60
    $ minigame_timer_running = False

    n "【遊戲一：逃出迷霧】即將開始，請所有小隊準備好小白板。"

    # 呼叫計時說明畫面
    call screen minigame_1_screen

    n "計時結束，請公布各小隊預測數值，並統計得分！"

    # 使用 return 返回主線劇情（script.rpy 中 call minigame_1 的下一行就是 label after_minigame_1）
    # 若使用 call after_minigame_1 會導致調用棧重複，遊戲結束時會重新執行一遍劇情。
    return

# ==========================================
# 小遊戲二：採椰子大賽 相關邏輯與畫面
# ==========================================
screen minigame_2_screen():
    modal True
    add Solid("#000000aa")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 680
        padding (40, 40)
        
        vbox:
            spacing 15
            xalign 0.5
            
            # 遊戲標題
            text "遊戲二 採椰子大賽 (最大唯一數)" size 36 color "#FFD700" xalign 0.5 bold True
            
            # 規則說明框
            frame:
                background Solid("#1c2230cc")
                padding (25, 25)
                xsize 820
                xalign 0.5
                
                vbox:
                    spacing 12
                    text "【遊戲規則】" size 26 bold True color "#4ECDC4"
                    text "每支小隊請在小白板上秘密寫下 1 ~ 15 之間的任一整數（代表要搶的椰子）。" size 20 color "#ffffff"
                    text "1. 撞車摔落（淘汰）" size 22 color "#ff6666" bold True
                    text "   只要寫下的數字與「任何其他小隊」重複，發生重複的小隊全數出局，本局得 0 分。" size 20 color "#ffffff"
                    text "2. 高樹採收（得分）" size 22 color "#fcd34d" bold True
                    text "   排除掉所有重複的數字後，在剩下的「唯一數字」中進行排名。" size 20 color "#ffffff"
                    text "   數字最大的前三名小隊，依序獲得 3 分、2 分、1 分。" size 20 color "#ffffff"
            
            null height 5
            
            # 計時器展示與控制區 (縮小元件)
            vbox:
                spacing 8
                xalign 0.5
                
                # 倒數計時顯示 (從 48 縮小至 32)
                text "[minigame_timer_value] 秒" size 32 color "#ff5555" xalign 0.5 bold True
                
                # 時間進度條 (縮短且變細)
                bar:
                    value minigame_timer_value
                    range minigame_timer_duration
                    xalign 0.5
                    xsize 350
                    ysize 8
                
                # 設定時間面板 (字型縮小至 14)
                if not minigame_timer_running:
                    hbox:
                        spacing 10
                        xalign 0.5
                        yalign 0.5
                        text "設定倒數時間：" size 14 color "#cccccc" yalign 0.5
                        
                        textbutton "30 秒" action [SetVariable("minigame_timer_duration", 30), SetVariable("minigame_timer_value", 30)] text_size 14
                        textbutton "60 秒" action [SetVariable("minigame_timer_duration", 60), SetVariable("minigame_timer_value", 60)] text_size 14
                        textbutton "90 秒" action [SetVariable("minigame_timer_duration", 90), SetVariable("minigame_timer_value", 90)] text_size 14
                        textbutton "120 秒" action [SetVariable("minigame_timer_duration", 120), SetVariable("minigame_timer_value", 120)] text_size 14
                        
                        hbox:
                            spacing 3
                            textbutton "-10" action [SetVariable("minigame_timer_duration", max(10, minigame_timer_duration - 10)), SetVariable("minigame_timer_value", max(10, minigame_timer_value - 10))] text_size 14
                            textbutton "+10" action [SetVariable("minigame_timer_duration", minigame_timer_duration + 10), SetVariable("minigame_timer_value", minigame_timer_value + 10)] text_size 14
                
                # 計時器控制按鈕 (字型縮小至 16)
                hbox:
                    spacing 20
                    xalign 0.5
                    
                    if not minigame_timer_running:
                        textbutton "開始計時" action SetVariable("minigame_timer_running", True) text_color "#4ECDC4" text_size 16
                    else:
                        textbutton "暫停計時" action SetVariable("minigame_timer_running", False) text_color "#ffb6b6" text_size 16
                        
                    textbutton "重設時間" action [SetVariable("minigame_timer_running", False), SetVariable("minigame_timer_value", minigame_timer_duration)] text_size 16
            
            null height 10
            
            # 開始與下一步 (字型縮小至 18)
            textbutton "關閉說明，繼續劇情" action Return() xalign 0.5 text_size 18 text_color "#ffffff" text_hover_color "#FFD700"

    # 計時器觸發器邏輯
    if minigame_timer_running and minigame_timer_value > 0:
        timer 1.0 action SetVariable("minigame_timer_value", minigame_timer_value - 1) repeat True
    elif minigame_timer_running and minigame_timer_value <= 0:
        timer 0.1 action [SetVariable("minigame_timer_running", False), Notify("時間到！時間已結束！")]

label minigame_2:
    $ minigame_timer_duration = 60
    $ minigame_timer_value = 60
    $ minigame_timer_running = False

    n "【遊戲二：採椰子大賽】即將開始，請各小隊準備好小白板。"
    call screen minigame_2_screen
    n "計時結束，請公布各小隊選擇的椰子，並統計得分！"
    return

# ==========================================
# 小遊戲三：我有一個淘金夢(改) 相關邏輯與畫面
# ==========================================
screen minigame_3_screen():
    modal True
    add Solid("#000000aa")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 760
        padding (40, 40)
        
        vbox:
            spacing 15
            xalign 0.5
            
            # 遊戲標題
            text "遊戲三 我有一個淘金夢" size 36 color "#FFD700" xalign 0.5 bold True
            
            # 規則說明框
            frame:
                background Solid("#1c2230cc")
                padding (25, 25)
                xsize 820
                xalign 0.5
                
                vbox:
                    spacing 12
                    text "【遊戲規則】" size 26 bold True color "#4ECDC4"
                    text "每隊在小白板上寫下 A、B、C 其中一個代號，代表要挖的礦場。" size 20 color "#ffffff"
                    text "各礦場價值與容量限制如下：" size 20 color "#ffffff"
                    text "A 礦場：金礦，價值 3 分（最多容納 2 隊）" size 20 color "#fcd34d" bold True
                    text "B 礦場：銀礦，價值 2 分（最多容納 3 隊）" size 20 color "#c0c0c0" bold True
                    text "C 礦場：銅礦，價值 1 分（最多容納 6 隊）" size 20 color "#cd7f32" bold True
                    text "若前往某礦場的隊伍數「超過」該礦場容納上限，礦場將會崩塌！" size 20 color "#ff5555" bold True
                    text "崩塌礦場內的隊伍皆得 0 分。未崩塌礦場內的隊伍則可獲得對應分數。" size 20 color "#ffffff"
            
            null height 5
            
            # 計時器展示與控制區 (縮小元件)
            vbox:
                spacing 8
                xalign 0.5
                
                # 倒數計時顯示 (從 48 縮小至 32)
                text "[minigame_timer_value] 秒" size 32 color "#ff5555" xalign 0.5 bold True
                
                # 時間進度條 (縮短且變細)
                bar:
                    value minigame_timer_value
                    range minigame_timer_duration
                    xalign 0.5
                    xsize 350
                    ysize 8
                
                # 設定時間面板 (字型縮小至 14)
                if not minigame_timer_running:
                    hbox:
                        spacing 10
                        xalign 0.5
                        yalign 0.5
                        text "設定倒數時間：" size 14 color "#cccccc" yalign 0.5
                        
                        textbutton "30 秒" action [SetVariable("minigame_timer_duration", 30), SetVariable("minigame_timer_value", 30)] text_size 14
                        textbutton "60 秒" action [SetVariable("minigame_timer_duration", 60), SetVariable("minigame_timer_value", 60)] text_size 14
                        textbutton "90 秒" action [SetVariable("minigame_timer_duration", 90), SetVariable("minigame_timer_value", 90)] text_size 14
                        textbutton "120 秒" action [SetVariable("minigame_timer_duration", 120), SetVariable("minigame_timer_value", 120)] text_size 14
                        
                        hbox:
                            spacing 3
                            textbutton "-10" action [SetVariable("minigame_timer_duration", max(10, minigame_timer_duration - 10)), SetVariable("minigame_timer_value", max(10, minigame_timer_value - 10))] text_size 14
                            textbutton "+10" action [SetVariable("minigame_timer_duration", minigame_timer_duration + 10), SetVariable("minigame_timer_value", minigame_timer_value + 10)] text_size 14
                
                # 計時器控制按鈕 (字型縮小至 16)
                hbox:
                    spacing 20
                    xalign 0.5
                    
                    if not minigame_timer_running:
                        textbutton "開始計時" action SetVariable("minigame_timer_running", True) text_color "#4ECDC4" text_size 16
                    else:
                        textbutton "暫停計時" action SetVariable("minigame_timer_running", False) text_color "#ffb6b6" text_size 16
                        
                    textbutton "重設時間" action [SetVariable("minigame_timer_running", False), SetVariable("minigame_timer_value", minigame_timer_duration)] text_size 16
            
            null height 10
            
            # 開始與下一步 (字型縮小至 18)
            textbutton "關閉說明，繼續劇情" action Return() xalign 0.5 text_size 18 text_color "#ffffff" text_hover_color "#FFD700"

    # 計時器觸發器邏輯
    if minigame_timer_running and minigame_timer_value > 0:
        timer 1.0 action SetVariable("minigame_timer_value", minigame_timer_value - 1) repeat True
    elif minigame_timer_running and minigame_timer_value <= 0:
        timer 0.1 action [SetVariable("minigame_timer_running", False), Notify("時間到！時間已結束！")]

label minigame_3:
    $ minigame_timer_duration = 60
    $ minigame_timer_value = 60
    $ minigame_timer_running = False

    n "【遊戲三：我有一個淘金夢】即將開始，請各小隊準備好小白板。"
    call screen minigame_3_screen
    n "計時結束，請公布各小隊要挖的礦場，並統計得分！"
    return

# ==========================================
# 小遊戲四：越獄行動 相關邏輯與畫面
# ==========================================
screen minigame_4_screen():
    modal True
    add Solid("#000000aa")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 760
        padding (40, 40)
        
        vbox:
            spacing 15
            xalign 0.5
            
            # 遊戲標題
            text "遊戲四 越獄行動" size 36 color "#FFD700" xalign 0.5 bold True
            
            # 規則說明框
            frame:
                background Solid("#1c2230cc")
                padding (25, 25)
                xsize 820
                xalign 0.5
                
                vbox:
                    spacing 8
                    text "【遊戲規則】" size 26 bold True color "#4ECDC4"
                    text "每支小隊在小白板秘密寫下 0 ~ 10 的整數，代表逃獄速度與動靜大小。" size 20 color "#ffffff"
                    text "公佈後計算全場數字和（總動靜）：" size 20 color "#ffffff"
                    text "1. 神不知鬼不覺（總和小於等於60）" size 22 color "#aed8f2" bold True
                    text "   守衛沒有起疑。數字最大（速度最快）的前三名小隊，" size 20 color "#ffffff"
                    text "   率先抵達碼頭搶走最好的三艘船，依序獲 3 分、2 分、1 分。" size 20 color "#ffffff"
                    text "2. 警鈴大作（總和超過60）" size 22 color "#ff6666" bold True
                    text "   動靜過大被守衛發現！數字最小（最慢）的三個小隊及時退回，" size 20 color "#ffffff"
                    text "   趁亂從後門溜出，數字由小到大獲得 3 分、2 分、1 分。" size 20 color "#ffffff"
            
            null height 5
            
            # 計時器展示與控制區 (縮小元件)
            vbox:
                spacing 8
                xalign 0.5
                
                # 倒數計時顯示 (從 48 縮小至 32)
                text "[minigame_timer_value] 秒" size 32 color "#ff5555" xalign 0.5 bold True
                
                # 時間進度條 (縮短且變細)
                bar:
                    value minigame_timer_value
                    range minigame_timer_duration
                    xalign 0.5
                    xsize 350
                    ysize 8
                
                # 設定時間面板 (字型縮小至 14)
                if not minigame_timer_running:
                    hbox:
                        spacing 10
                        xalign 0.5
                        yalign 0.5
                        text "設定倒數時間：" size 14 color "#cccccc" yalign 0.5
                        
                        textbutton "30 秒" action [SetVariable("minigame_timer_duration", 30), SetVariable("minigame_timer_value", 30)] text_size 14
                        textbutton "60 秒" action [SetVariable("minigame_timer_duration", 60), SetVariable("minigame_timer_value", 60)] text_size 14
                        textbutton "90 秒" action [SetVariable("minigame_timer_duration", 90), SetVariable("minigame_timer_value", 90)] text_size 14
                        textbutton "120 秒" action [SetVariable("minigame_timer_duration", 120), SetVariable("minigame_timer_value", 120)] text_size 14
                        
                        hbox:
                            spacing 3
                            textbutton "-10" action [SetVariable("minigame_timer_duration", max(10, minigame_timer_duration - 10)), SetVariable("minigame_timer_value", max(10, minigame_timer_value - 10))] text_size 14
                            textbutton "+10" action [SetVariable("minigame_timer_duration", minigame_timer_duration + 10), SetVariable("minigame_timer_value", minigame_timer_value + 10)] text_size 14
                
                # 計時器控制按鈕 (字型縮小至 16)
                hbox:
                    spacing 20
                    xalign 0.5
                    
                    if not minigame_timer_running:
                        textbutton "開始計時" action SetVariable("minigame_timer_running", True) text_color "#4ECDC4" text_size 16
                    else:
                        textbutton "暫停計時" action SetVariable("minigame_timer_running", False) text_color "#ffb6b6" text_size 16
                        
                    textbutton "重設時間" action [SetVariable("minigame_timer_running", False), SetVariable("minigame_timer_value", minigame_timer_duration)] text_size 16
            
            null height 10
            
            # 開始與下一步 (字型縮小至 18)
            textbutton "關閉說明，繼續劇情" action Return() xalign 0.5 text_size 18 text_color "#ffffff" text_hover_color "#FFD700"

    # 計時器觸發器邏輯
    if minigame_timer_running and minigame_timer_value > 0:
        timer 1.0 action SetVariable("minigame_timer_value", minigame_timer_value - 1) repeat True
    elif minigame_timer_running and minigame_timer_value <= 0:
        timer 0.1 action [SetVariable("minigame_timer_running", False), Notify("時間到！時間已結束！")]

label minigame_4:
    $ minigame_timer_duration = 60
    $ minigame_timer_value = 60
    $ minigame_timer_running = False

    n "【遊戲四：越獄行動】即將開始，請各小隊準備好小白板。"
    call screen minigame_4_screen
    n "計時結束，請公布各小隊逃獄速度，並統計得分！"
    return

# ==========================================
# 小遊戲五：毒氣中的橫財 相關邏輯與畫面
# ==========================================
screen minigame_5_screen():
    modal True
    add Solid("#000000aa")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 760
        padding (40, 40)
        
        vbox:
            spacing 15
            xalign 0.5
            
            # 遊戲標題
            text "遊戲五 毒氣中的橫財" size 36 color "#FFD700" xalign 0.5 bold True
            
            # 規則說明框
            frame:
                background Solid("#1c2230cc")
                padding (25, 25)
                xsize 820
                xalign 0.5
                
                vbox:
                    spacing 8
                    text "【遊戲規則】" size 26 bold True color "#4ECDC4"
                    text "秘密寫下 0 ~ 300 的整數（代表進入山洞的秒數）。公佈後由小到大結算：" size 20 color "#ffffff"
                    text "1. 第一位抵達者（啟動機關）" size 22 color "#fcd34d" bold True
                    text "   寫下「最小數字」的小隊取走毒瘴水晶，獲得「時間 / 10」分（平手則平分）。" size 20 color "#ffffff"
                    text "   同時啟動抽風機，需等待 60 秒 毒氣才會抽光並解鎖寶物。" size 20 color "#ffffff"
                    text "2. 後續抵達者（搶奪寶物）" size 22 color "#aed8f2" bold True
                    text "   在毒氣散去（即「啟動秒數 + 60 秒」）後，最先進入的前三名搶得洞內的精緻裝備，分別獲得 3、2、1 分。" size 20 color "#ffffff"
                    text "3. 提早進入（中毒淘汰）" size 22 color "#ff6666" bold True
                    text "   除第一位外，任何在毒氣未散去前就進入的小隊，皆得 0 分。" size 20 color "#ffffff"
            
            null height 5
            
            # 計時器展示與控制區 (縮小元件)
            vbox:
                spacing 8
                xalign 0.5
                
                # 倒數計時顯示 (從 48 縮小至 32)
                text "[minigame_timer_value] 秒" size 32 color "#ff5555" xalign 0.5 bold True
                
                # 時間進度條 (縮短且變細)
                bar:
                    value minigame_timer_value
                    range minigame_timer_duration
                    xalign 0.5
                    xsize 350
                    ysize 8
                
                # 設定時間面板 (字型縮小至 14)
                if not minigame_timer_running:
                    hbox:
                        spacing 10
                        xalign 0.5
                        yalign 0.5
                        text "設定倒數時間：" size 14 color "#cccccc" yalign 0.5
                        
                        textbutton "30 秒" action [SetVariable("minigame_timer_duration", 30), SetVariable("minigame_timer_value", 30)] text_size 14
                        textbutton "60 秒" action [SetVariable("minigame_timer_duration", 60), SetVariable("minigame_timer_value", 60)] text_size 14
                        textbutton "90 秒" action [SetVariable("minigame_timer_duration", 90), SetVariable("minigame_timer_value", 90)] text_size 14
                        textbutton "120 秒" action [SetVariable("minigame_timer_duration", 120), SetVariable("minigame_timer_value", 120)] text_size 14
                        
                        hbox:
                            spacing 3
                            textbutton "-10" action [SetVariable("minigame_timer_duration", max(10, minigame_timer_duration - 10)), SetVariable("minigame_timer_value", max(10, minigame_timer_value - 10))] text_size 14
                            textbutton "+10" action [SetVariable("minigame_timer_duration", minigame_timer_duration + 10), SetVariable("minigame_timer_value", minigame_timer_value + 10)] text_size 14
                
                # 計時器控制按鈕 (字型縮小至 16)
                hbox:
                    spacing 20
                    xalign 0.5
                    
                    if not minigame_timer_running:
                        textbutton "開始計時" action SetVariable("minigame_timer_running", True) text_color "#4ECDC4" text_size 16
                    else:
                        textbutton "暫停計時" action SetVariable("minigame_timer_running", False) text_color "#ffb6b6" text_size 16
                        
                    textbutton "重設時間" action [SetVariable("minigame_timer_running", False), SetVariable("minigame_timer_value", minigame_timer_duration)] text_size 16
            
            null height 10
            
            # 開始與下一步 (字型縮小至 18)
            textbutton "關閉說明，繼續劇情" action Return() xalign 0.5 text_size 18 text_color "#ffffff" text_hover_color "#FFD700"

    # 計時器觸發器邏輯
    if minigame_timer_running and minigame_timer_value > 0:
        timer 1.0 action SetVariable("minigame_timer_value", minigame_timer_value - 1) repeat True
    elif minigame_timer_running and minigame_timer_value <= 0:
        timer 0.1 action [SetVariable("minigame_timer_running", False), Notify("時間到！時間已結束！")]

label minigame_5:
    $ minigame_timer_duration = 60
    $ minigame_timer_value = 60
    $ minigame_timer_running = False

    n "【遊戲五：毒氣中的橫財】即將開始，請各小隊準備好小白板。"
    call screen minigame_5_screen
    n "計時結束，請公布各小隊進入秒數，並統計得分！"
    return

# ==========================================
# 小遊戲六：通往天國的倒數計時 相關邏輯與畫面
# ==========================================
screen minigame_6_screen():
    modal True
    add Solid("#000000aa")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 760
        padding (40, 40)
        
        vbox:
            spacing 15
            xalign 0.5
            
            # 遊戲標題
            text "遊戲六 通往天國的倒數計時" size 36 color "#FFD700" xalign 0.5 bold True
            
            # 規則說明框
            frame:
                background Solid("#1c2230cc")
                padding (25, 25)
                xsize 820
                xalign 0.5
                
                vbox:
                    spacing 8
                    text "【遊戲規則】" size 26 bold True color "#4ECDC4"
                    text "填入 0~600 的整數 t0，代表在第 t0 秒你們進入財寶庫，將前人踢出並搜刮寶物。" size 20 color "#ffffff"
                    text "1. 搜刮與被踢出" size 22 color "#fcd34d" bold True
                    text "   直到下一個人在 t1 秒進來將你踢出前，你將獲得 (t1 - t0) 份的財寶。" size 20 color "#ffffff"
                    text "   最後一個進入的小隊將一直搜刮到第 600 秒為止。" size 20 color "#ffffff"
                    text "2. 同時進入的平分機制" size 22 color "#aed8f2" bold True
                    text "   如果有 k 個人在同一秒 t0 同時進來，他們將各分得 (t1 - t0) / k 份財寶。" size 20 color "#ffffff"
                    text "3. 積分結算" size 22 color "#ff6666" bold True
                    text "   結算後，獲取財寶總數最多的前三名隊伍，將分別獲得 3 分、2 分、1 分。" size 20 color "#ffffff"
            
            null height 5
            
            # 計時器展示與控制區 (縮小元件)
            vbox:
                spacing 8
                xalign 0.5
                
                # 倒數計時顯示 (從 48 縮小至 32)
                text "[minigame_timer_value] 秒" size 32 color "#ff5555" xalign 0.5 bold True
                
                # 時間進度條 (縮短且變細)
                bar:
                    value minigame_timer_value
                    range minigame_timer_duration
                    xalign 0.5
                    xsize 350
                    ysize 8
                
                # 設定時間面板 (字型縮小至 14)
                if not minigame_timer_running:
                    hbox:
                        spacing 10
                        xalign 0.5
                        yalign 0.5
                        text "設定倒數時間：" size 14 color "#cccccc" yalign 0.5
                        
                        textbutton "30 秒" action [SetVariable("minigame_timer_duration", 30), SetVariable("minigame_timer_value", 30)] text_size 14
                        textbutton "60 秒" action [SetVariable("minigame_timer_duration", 60), SetVariable("minigame_timer_value", 60)] text_size 14
                        textbutton "90 秒" action [SetVariable("minigame_timer_duration", 90), SetVariable("minigame_timer_value", 90)] text_size 14
                        textbutton "120 秒" action [SetVariable("minigame_timer_duration", 120), SetVariable("minigame_timer_value", 120)] text_size 14
                        
                        hbox:
                            spacing 3
                            textbutton "-10" action [SetVariable("minigame_timer_duration", max(10, minigame_timer_duration - 10)), SetVariable("minigame_timer_value", max(10, minigame_timer_value - 10))] text_size 14
                            textbutton "+10" action [SetVariable("minigame_timer_duration", minigame_timer_duration + 10), SetVariable("minigame_timer_value", minigame_timer_value + 10)] text_size 14
                
                # 計時器控制按鈕 (字型縮小至 16)
                hbox:
                    spacing 20
                    xalign 0.5
                    
                    if not minigame_timer_running:
                        textbutton "開始計時" action SetVariable("minigame_timer_running", True) text_color "#4ECDC4" text_size 16
                    else:
                        textbutton "暫停計時" action SetVariable("minigame_timer_running", False) text_color "#ffb6b6" text_size 16
                        
                    textbutton "重設時間" action [SetVariable("minigame_timer_running", False), SetVariable("minigame_timer_value", minigame_timer_duration)] text_size 16
            
            null height 10
            
            # 開始與下一步 (字型縮小至 18)
            textbutton "關閉說明，繼續劇情" action Return() xalign 0.5 text_size 18 text_color "#ffffff" text_hover_color "#FFD700"

    # 計時器觸發器邏輯
    if minigame_timer_running and minigame_timer_value > 0:
        timer 1.0 action SetVariable("minigame_timer_value", minigame_timer_value - 1) repeat True
    elif minigame_timer_running and minigame_timer_value <= 0:
        timer 0.1 action [SetVariable("minigame_timer_running", False), Notify("時間到！時間已結束！")]

label minigame_6:
    $ minigame_timer_duration = 60
    $ minigame_timer_value = 60
    $ minigame_timer_running = False

    n "【遊戲六：通往天國的倒數計時】即將開始，請各小隊準備好小白板。"
    call screen minigame_6_screen
    n "計時結束，請公布各小隊進入時間，並統計得分！"
    return