# ==========================================
# 角色與立繪定義
# ==========================================
# 定義角色，並關聯立繪標籤
define f = Character("傲嬌女船長", image="female_captain", color="#ff6666") # 暴躁、口嫌體正直、死愛錢
define m = Character("腹黑男船長", image="male_captain", color="#6699ff") # 總在旁邊說風涼話、笑面虎
define e = Character("部落長老", image="elder", color="#339933")   # 威嚴、守護島嶼
define n = Character("旁白", color="#cccccc")      # 描述環境與過場

# 定義紫色霧氣效果 (半透明紫色 Solid 色塊)
image purple_fog = Solid("#8a2be240")

# 定義微弱的閃爍金光效果 (呼吸燈動畫)
image golden_glow_pulse:
    "images/golden_glow.png"
    anchor (0.5, 0.5)
    # 在 40% 到 90% 透明度之間緩慢變化
    alpha 0.4
    easein 3.0 alpha 0.9
    easeout 3.0 alpha 0.4
    repeat

# 定義自動縮放到 1920x1080 解析度的背景圖片
image bg ocean:
    "images/bg ocean.jpg"
    xysize (1920, 1080)

image bg island:
    "images/bg island.jpg"
    xysize (1920, 1080)

image bg ocean_fog:
    "images/bg ocean_fog.jpg"
    xysize (1920, 1080)

image bg beach:
    "images/bg beach.jpg"
    xysize (1920, 1080)

image bg forest:
    "images/bg forest.jpg"
    xysize (1920, 1080)

image bg prison:
    "images/bg prison.jpg"
    xysize (1920, 1080)

image bg beach_night:
    "images/bg beach_night.jpg"
    xysize (1920, 1080)

image bg cave_entrance:
    "images/bg cave_entrance.jpg"
    xysize (1920, 1080)

image bg secret_room:
    "images/bg secret_room.jpg"
    xysize (1920, 1080)

# ==========================================
# 故事主程式
# ==========================================
label start:

    # ------------------------------------------
    # 【前情提要 & 故事開始】
    # ------------------------------------------
    # 顯示海洋背景，淡入
    scene bg ocean with fade
    
    n "大海上，十艘海盜船正浩浩蕩蕩地共同航行著。名面上，這是一支為了尋找傳說祕寶而結成的同盟艦隊……"
    n "但實際上，每個人都各懷鬼胎，暗潮洶湧。"

    scene bg island with fade
    # 顯示女船長（生氣表情）在左側，並伴隨震動效果
    show female_captain angry at left with dissolve
    f "（拍桌）喂！航行了大半年，前面總算出現一座小島了！這座標跟航海圖上的祕寶位置完全吻合！"
    
    # 讓女船長變更為得意/高興表情
    show female_captain happy at left
    f "傳令下去，全速前進！本小姐絕對要第一個登島，誰敢跟我搶，我就轟沉他的船！"

    # 顯示男船長（微笑表情）在右側
    show male_captain smile at right with dissolve
    m "（輕笑）哎呀呀，我們的女船長還是一如既往地暴躁呢。表面上大家可是『好夥伴』，妳這樣吃獨食，其他八艘船的船長可是會傷心的喔。"
    
    # 男船長切換為無奈/調侃表情
    show male_captain helpless at right
    m "（推眼鏡）雖然……我也沒打算把財寶讓給妳就是了。"

    show female_captain angry at left
    f "哼！少囉嗦！誰跟你們是好夥伴了，我只是利用你們……等等，前面怎麼回事？"

    # 切換背景到起霧的海洋，使用較慢的淡入效果
    scene bg ocean_fog with fade
    show female_captain shocked at left
    show male_captain serious at right
    with dissolve

    n "話音未落，海面上突然泛起一陣詭異的濃霧，瞬間吞噬了前方的視野，十艘船在霧中被迫分散。"

    m "看來這座島，不太想讓我們輕易靠近呢。各位各懷鬼胎的船長們，祝你們好運囉。"

    # 隱藏角色立繪，準備切換至小遊戲
    hide female_captain
    hide male_captain
    with dissolve

    # [小遊戲一：濃霧航海]
    # 請將 minigame_1 替換為你實際的小遊戲標籤
    call minigame_1 

    # ------------------------------------------
    # 【登島】
    # ------------------------------------------
    label after_minigame_1:
        # 切換到沙灘背景
        scene bg beach with fade
        
        n "縱使在濃霧中有著不同的航線選擇，你們最終還是都登上了島嶼。"
        n "然而，映入眼簾的卻是一望無際的白沙灘，以及一排整齊劃一的椰子樹。"

        show female_captain angry at left with dissolve
        f "哈！？你確定這是祕寶所在地？沙灘？椰子樹？我們是來度假的嗎！可惡，我的黃金呢！"

        show male_captain smile at right with dissolve
        m "（伸懶腰）度假也不錯啊，妳看這海風多舒服。打打殺殺那麼久，就當作是來放鬆……"

        # 畫面產生劇烈左右震動，代表起大風
        with hpunch
        n "突然間，一陣強烈的大風吹過。"
        n "沙沙沙——那一排椰子樹劇烈晃動，緊接著，一堆大小不一的椰子從樹上掉了下來！"

        show female_captain shocked at left
        f "哎喲！什麼東西掉下來了！……等、等等，這光澤是怎麼回事？"

        show male_captain surprised at right
        m "（撿起一看，挑眉）金燦燦的……椰子？看來這可不是什麼單純的度假勝地啊，事情變得有趣起來了。"

    # 隱藏角色，切換至小遊戲二
    hide female_captain
    hide male_captain
    with dissolve

    # [小遊戲二：接椰子/開椰子]
    call minigame_2

    # ------------------------------------------
    # 【挖挖挖礦】
    # ------------------------------------------
    label after_minigame_2:
        # 切換到叢林/原住民聚落附近背景
        scene bg forest with fade
        
        n "開完金椰子後，心滿意足的你們開始深入勘查整個島嶼。"
        n "在穿過一片叢林後，你們躲在草叢後方，發現島上竟然有一群原住民，而他們的聚落附近，赫然佇立著三座巨大的礦場！"
        
        show female_captain happy at left with dissolve
        f "（雙眼發光）快看！是礦場！而且足足有三座！發財了發財了！"

        show male_captain serious at right with dissolve
        m "噓，妳小聲點。沒看到礦坑旁邊有原住民在巡邏嗎？看這陣仗，那些礦場顯然是他們的財產。"

        show female_captain angry at left
        f "那又怎樣？我們可是海盜！海盜的字典裡沒有『別人的』這三個字！"
        f "管他是誰的，我看到的，統統都是我的！準備動手！"

        show male_captain smile at right
        m "呵呵，真是簡單粗暴的強盜邏輯。不過……我並不討厭這個提議。"

    hide female_captain
    hide male_captain
    with dissolve

    # [小遊戲三：挖礦/潛行搶奪]
    call minigame_3

    # ------------------------------------------
    # 【挖！出事了】
    # ------------------------------------------
    label after_minigame_3:
        # 維持叢林背景
        scene bg forest
        
        n "正當你們口袋裝滿黃金，腦海裡已經開始幻想著要拿這筆橫財去哪裡大肆揮霍時……"
        
        # 部落長老登場
        show elder normal at center with dissolve
        n "周圍突然湧出大量的原住民，將你們團團包圍！"

        show elder angry at center
        e "無知的闖入者！竟敢覬覦我們部落的神聖金礦！"
        e "把這些貪婪的海盜全給我五花大綁，丟進地牢裡！"

        # 切換到地牢背景，淡入
        scene bg prison with fade

        n "雙拳難敵四手，你們被毫不留情地扔進了陰暗的監牢裡。"

        show female_captain angry at left with dissolve
        f "（掙扎）放開我！你這臭老頭！等我出去，我一定要把你的鬍子全拔光！我的金幣啊——！"

        show male_captain helpless at right with dissolve
        m "（無奈嘆氣）哎呀呀，剛剛是誰信誓旦旦地說『統統都是我的』？現在連自己都被綁得像顆粽子了。"

        show female_captain angry at left
        f "你給我閉嘴！你這腹黑男除了說風涼話還會幹嘛？快想辦法弄開這繩子！"

        show male_captain smile at right
        m "別急嘛。區區一個小破監牢，怎麼可能攔得住我們這些『偉大』的海盜？"
        m "今晚夜色不錯，正適合來一場……瘋狂的越獄行動。準備好了嗎，女船長？"

    hide female_captain
    hide male_captain
    with dissolve

    # [小遊戲四：越獄/解謎逃脫]
    call minigame_4

    # ------------------------------------------
    # 【逃離村莊】
    # ------------------------------------------
    label after_minigame_4:
        # 切換回夜晚的沙灘/外圍路徑背景
        scene bg beach_night with fade
        
        n "在一陣兵荒馬亂與混亂之中，你們最終成功騙過守衛，逃離了監獄。"

        show female_captain tired at left with dissolve
        f "呼……呼……終於甩掉那些傢伙了。可惡，就這樣空手離開，我怎麼嚥得下這口氣！"

        show male_captain serious at right with dissolve
        m "噓，先別抱怨了。妳看前面那座山洞……是不是有點不太對勁？"

        # 切換到山洞入口背景
        scene bg cave_entrance with dissolve
        
        n "順著視線望去，一座隱蔽的山洞引起了你們的注意。"
        
        # 顯示洞內金光與淡紫色霧氣覆蓋效果
        show golden_glow_pulse:
            xalign 0.44 yalign 0.63 zoom 0.5
        show purple_fog with dissolve
        show female_captain surprised at left
        show male_captain serious at right
        with dissolve

        n "山洞內瀰漫著詭異的紫色霧氣，霧氣中隱隱約約有誘人的金光在閃動。而在洞外，竟然架著一具古怪的抽風機，上頭還鑲著一顆搖搖欲墜的紫色晶體，正沐浴在霧氣中慢慢變大。"

        show female_captain shocked at left
        f "紫色的霧？還有抽風機？這座島上的科技樹也太奇怪了吧！"
        f "不過……那裡面閃爍的光芒，絕對是極品財寶的味道！"

        show male_captain smile at right
        m "看來這顆紫水晶在吸收霧氣成長……裡面藏著的東西，恐怕比外面的金礦還要驚人。走吧，去探探虛實。"

    hide female_captain
    hide male_captain
    with dissolve

    # [小遊戲五：閃避紫霧/操作抽風機]
    call minigame_5

    # ------------------------------------------
    # 【It's my goal!!】
    # ------------------------------------------
    label after_minigame_5:
        # 切換至神祕地下密室背景
        scene bg secret_room with fade
        
        n "金燦燦的裝備後，是一條綿延、伴隨著微弱亮光的小路。"
        n "你們順著這條小路，來到了一間隱密的地下密室。"

        show male_captain smile at right with dissolve

        show female_captain happy at left with dissolve
        f "（目瞪口呆）哇……你快看這密室！全都是金燦燦的財寶！這光芒！這觸感！我們以後的美好生活……"

        # 畫面產生劇烈上下震動，模擬地震
        with vpunch
        n "正當你們沉浸在暴富的幻想中時，整個山洞突然發出震耳欲聾的轟鳴聲！"
        n "轟隆隆——地面開始劇烈晃動，層層土石從天花板剝落砸下！"

        # 播放長老迴音，不顯示立繪，只顯示文字，或讓長老半透明出現
        e "（洞外傳來長老的迴音）愚蠢的海盜！你們觸動了島嶼的心臟！神明的憤怒將把你們永遠埋葬！"

        show male_captain serious at right
        m "（收起笑容，神情嚴肅）看來妳的美好生活得先按下暫停鍵了。這座山要塌了！"

        show female_captain angry at left
        f "開什麼玩笑！財寶就在眼前，我怎麼可能放棄！"
        f "管他的山崩地裂！給我十分鐘！我頂多再拿十分鐘就要衝出去！"

        show male_captain serious at right
        m "要是十分鐘沒逃出去，我們可就要永遠留在這裡給這些金子陪葬了。"
        
        show male_captain smile at right
        m "倒數計時開始了，能拿多少各憑本事吧，各位！"

    hide female_captain
    hide male_captain
    with dissolve

    # [小遊戲六：限時逃脫/抓寶]
    call minigame_6

    # 遊戲結束或結尾畫面
    label game_over:
        scene black with fade
        n "就這樣，海盜們的瘋狂大冒險畫下了句點……"
        return