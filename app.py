import streamlit as st

# ============================================================
# 拾光職涯｜MBTI 70 題電子測驗
# ============================================================

st.set_page_config(
    page_title="拾光職涯｜MBTI 70 題測驗",
    page_icon="🧭",
    layout="centered",
)

# ============================================================
# 70 題題庫
# ============================================================

QUESTIONS = [
    {"q": 1, "text": "在平常宴會中，你通常比較習慣於", "a": "和很多人交談、聊天，包括陌生人", "b": "只和少數認識的人交談", "dim": "EI"},
    {"q": 2, "text": "你比較", "a": "喜歡實際的事物多於運用想像力", "b": "重視想像來探索事物的意義", "dim": "SN"},
    {"q": 3, "text": "你認為何者說得對？", "a": "太多用想像容易忽略實際的問題", "b": "若是生活總是按常規做事會很無聊", "dim": "SN"},
    {"q": 4, "text": "下列何者影響你較深：", "a": "做事講求原則", "b": "情感、情緒及人際關係", "dim": "TF"},
    {"q": 5, "text": "你比較容易", "a": "能以理說服別人，令人無話可說", "b": "容易被別人感動", "dim": "TF"},
    {"q": 6, "text": "在工作上，你通常喜歡", "a": "有一定的期限和適當的進度表", "b": "沒有一定的時間表，只要能完成就可以", "dim": "JP"},
    {"q": 7, "text": "在選擇事物時，你比較多是", "a": "小心謹慎地加以選擇", "b": "容易衝動或隨當時的心境而定", "dim": "JP"},
    {"q": 8, "text": "在一般宴會中，你通常是", "a": "很晚才走，而且精神總是不錯", "b": "較早走，不然會感到精神愈來愈疲倦", "dim": "EI"},
    {"q": 9, "text": "你比較容易受哪一種人吸引？", "a": "通達事理的、注重實際的人", "b": "富有想像力的人", "dim": "SN"},
    {"q": 10, "text": "下列何者比較引起你的興趣", "a": "目前的現實", "b": "將來的可能", "dim": "SN"},
    {"q": 11, "text": "在評斷別人時，你較容易受到何者的支配？", "a": "原則問題：注重規定與原則", "b": "處境問題：看情形辦事可因人而異", "dim": "TF"},
    {"q": 12, "text": "你處事為人比較傾向", "a": "客觀、重視目標，對事不對人", "b": "重視人際關係，對人不對事", "dim": "TF"},
    {"q": 13, "text": "你通常比較", "a": "嚴守時間、較準時", "b": "對時間較隨性", "dim": "JP"},
    {"q": 14, "text": "何者令你覺得比較苦惱？", "a": "事情沒照進度完成", "b": "工作都完成後無新任務", "dim": "JP"},
    {"q": 15, "text": "在你的群體中，你比較", "a": "屬於消息靈通人士", "b": "不太知道團體發生了什麼事情", "dim": "EI"},
    {"q": 16, "text": "對於日常事情的處理，你通常喜歡", "a": "按照一般人的慣例去做", "b": "按照自己創新的方法去做", "dim": "SN"},
    {"q": 17, "text": "你若寫文章，你會", "a": "平鋪主敘，按事實說、不拐彎抹角", "b": "用隱喻、比喻的寫法來加強表達", "dim": "SN"},
    {"q": 18, "text": "何者比較像你", "a": "思想的一致性", "b": "和諧的人際關係", "dim": "TF"},
    {"q": 19, "text": "你平時比較喜歡？", "a": "邏輯推理（做理性分析）", "b": "價值判斷（做情緒選擇）", "dim": "TF"},
    {"q": 20, "text": "你喜歡讓事情", "a": "塵埃落定，確定下來", "b": "保持彈性，隨機待變", "dim": "JP"},
    {"q": 21, "text": "你認為你自己是個", "a": "認真而有決斷力", "b": "隨遇而安", "dim": "JP"},
    {"q": 22, "text": "在打電話前你", "a": "很少先計劃要說些什麼", "b": "常事先準備並想想要說些什麼", "dim": "EI"},
    {"q": 23, "text": "「一件事實」就是", "a": "說明事實本身而已", "b": "講明事實背後的意義", "dim": "SN"},
    {"q": 24, "text": "你覺得「憑空想像」是", "a": "有點令人苦惱", "b": "相當引人入勝", "dim": "SN"},
    {"q": 25, "text": "你認為自己是個", "a": "頭腦相當冷靜、清晰的人", "b": "十分古道熱腸、富感情的人", "dim": "TF"},
    {"q": 26, "text": "哪一種情況你認為比較糟糕", "a": "不公平、不公義、不公正", "b": "殘酷無情、無憐憫心、無同情心", "dim": "TF"},
    {"q": 27, "text": "你通常希望事情的進行路線", "a": "經過仔細的挑選、計畫、選擇", "b": "大概方向即可，不經意的、碰碰運氣的", "dim": "JP"},
    {"q": 28, "text": "你覺得何者較好？", "a": "購物時能買到所要的東西", "b": "購物時東西多樣化，有較多的選擇性", "dim": "JP"},
    {"q": 29, "text": "你在人群裡面", "a": "主動找人談話、主動帶出話題", "b": "常安靜、等著別人找你談話", "dim": "EI"},
    {"q": 30, "text": "你認為「常識」是", "a": "通常蠻可靠，不太會有問題的", "b": "通常有待商榷，不太可靠", "dim": "SN"},
    {"q": 31, "text": "你覺得自己通常是", "a": "有耐心處理固定的工作", "b": "對每天固定的工作不太有耐心", "dim": "SN"},
    {"q": 32, "text": "在決定某件事情時你比較", "a": "依循一定的標準或原則來決定", "b": "以個人的喜好與感覺來決定", "dim": "TF"},
    {"q": 33, "text": "你認為你比較是", "a": "堅決果斷", "b": "溫和文雅、平易近人", "dim": "TF"},
    {"q": 34, "text": "你比較傾向於", "a": "具有組織能力，辦事有方法", "b": "有調適力及讓別人願意去做事的能力", "dim": "JP"},
    {"q": 35, "text": "下列何者會令你比較舒服", "a": "事情相當明確、有脈絡可循", "b": "事情有彈性、有磋商餘地", "dim": "JP"},
    {"q": 36, "text": "新知識及非慣常的往來讓你", "a": "感到喜歡、興奮而精神充沛", "b": "感到勉強、傷神", "dim": "EI"},
    {"q": 37, "text": "你通常是個", "a": "比較注重實際事務的人", "b": "比較創新求變的人", "dim": "SN"},
    {"q": 38, "text": "你比較注意", "a": "別人能做什麼", "b": "別人有什麼看法", "dim": "SN"},
    {"q": 39, "text": "何者令你比較滿意", "a": "把整件事情討論得十分徹底", "b": "討論一件事，能達成共織、彼此和氣", "dim": "TF"},
    {"q": 40, "text": "你比較會受什麼支配？", "a": "頭腦、理性", "b": "心腸、感覺", "dim": "TF"},
    {"q": 41, "text": "你比較傾向怎樣的工作？", "a": "有明確的計劃、有清楚的契約", "b": "沒有明確規定、自然的、非正式的", "dim": "JP"},
    {"q": 42, "text": "你通常會期望事情", "a": "有秩序的、有規則的", "b": "隨機、隨性、自由的出現", "dim": "JP"},
    {"q": 43, "text": "你認為", "a": "有多而不必深交的朋友", "b": "有深交而不必多的朋友", "dim": "EI"},
    {"q": 44, "text": "你行事為人比較容易", "a": "按事實，實事求是", "b": "按原則，信念主導", "dim": "SN"},
    {"q": 45, "text": "何者你較有興趣？", "a": "生產及分配", "b": "研究與設計", "dim": "SN"},
    {"q": 46, "text": "最令你感到開心的讚賞是", "a": "「你是個非常有邏輯的人」", "b": "「你是個感情非常豐富的人」", "dim": "TF"},
    {"q": 47, "text": "你覺得自己較屬於哪種特質？", "a": "毅然決然、意志堅定不搖動", "b": "全心投入、忠實的、充滿熱忱的", "dim": "TF"},
    {"q": 48, "text": "你通常比較傾向於", "a": "確定、不隨意變更的陳述", "b": "提案式的、暫時性、準備性的陳述", "dim": "JP"},
    {"q": 49, "text": "你覺得何時比較舒坦？", "a": "做出正確的判斷", "b": "讓事情自然發展", "dim": "JP"},
    {"q": 50, "text": "你通常和陌生人", "a": "很容易交談，可以談很多", "b": "可以交談，但只說一些話", "dim": "EI"},
    {"q": 51, "text": "你比較相信你自己的", "a": "經驗", "b": "預感、第六感", "dim": "SN"},
    {"q": 52, "text": "你覺得自己", "a": "較為實際、實用甚於發明創造", "b": "有發明創造的能力甚於實際應用", "dim": "SN"},
    {"q": 53, "text": "哪一種人比較令你欣賞", "a": "有清楚理智的人", "b": "有豐富情感的人", "dim": "TF"},
    {"q": 54, "text": "你比較傾向於", "a": "公平、公義", "b": "同情、體諒", "dim": "TF"},
    {"q": 55, "text": "何者比較像你", "a": "事情都有安排與計劃", "b": "隨性、船到橋頭自然直", "dim": "JP"},
    {"q": 56, "text": "在人際關係上大多數的事應該", "a": "溝通協商，甚至談判", "b": "不用刻意，隨遇而安", "dim": "JP"},
    {"q": 57, "text": "電話鈴響的時候你通常", "a": "第一個趕著去接", "b": "希望別人會去接", "dim": "EI"},
    {"q": 58, "text": "你認為自己哪一點較值得讚賞", "a": "具有強烈的現實感", "b": "具有豐富的想像力", "dim": "SN"},
    {"q": 59, "text": "你比較容易", "a": "注意基本、重要的、原理的事", "b": "注意寓意、弦外之音", "dim": "SN"},
    {"q": 60, "text": "下列何者是較大的錯誤", "a": "太感情用事", "b": "太注重客觀", "dim": "TF"},
    {"q": 61, "text": "你認為自己基本上是一個", "a": "冷靜的，腳踏實地的人", "b": "柔軟的，性情溫和的人", "dim": "TF"},
    {"q": 62, "text": "你比較喜歡哪一種情境", "a": "有計劃的、有進度表的", "b": "沒有計劃的、沒有進度表的", "dim": "JP"},
    {"q": 63, "text": "你是個比較將事情", "a": "循規蹈矩、例行公事", "b": "有很多新奇主意", "dim": "JP"},
    {"q": 64, "text": "你覺得你比較", "a": "放得開，讓人容易接近", "b": "保守，與人有些微隔閡或保持距離", "dim": "EI"},
    {"q": 65, "text": "在寫作時你比較喜愛", "a": "寫實不誇張，實實在在描寫", "b": "用比喻、象徵性、修飾的描寫", "dim": "SN"},
    {"q": 66, "text": "何者對你而較容易", "a": "使用別人的長處", "b": "認同別人的想法", "dim": "SN"},
    {"q": 67, "text": "你喜歡自己已經擁有", "a": "清晰的思維", "b": "感情的力量", "dim": "TF"},
    {"q": 68, "text": "你認為何者是較大的過錯", "a": "草率，任性妄為", "b": "挑剔，批評論斷", "dim": "TF"},
    {"q": 69, "text": "你過去的生活比較多", "a": "經過計劃的事", "b": "沒有經過計劃的事", "dim": "JP"},
    {"q": 70, "text": "你是個比較", "a": "深思熟慮的人", "b": "讓事情自然生發的人", "dim": "JP"},
]

# ============================================================
# MBTI 四大向度
# ============================================================

DIMENSIONS = {
    "EI": ("E", "I", "外向 E", "內向 I"),
    "SN": ("S", "N", "實感 S", "直覺 N"),
    "TF": ("T", "F", "思考 T", "情感 F"),
    "JP": ("J", "P", "判斷 J", "感知 P"),
}

# ============================================================
# Session State
# ============================================================

if "started" not in st.session_state:
    st.session_state.started = False

if "current" not in st.session_state:
    st.session_state.current = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "finished" not in st.session_state:
    st.session_state.finished = False

if "show_answers" not in st.session_state:
    st.session_state.show_answers = False


# ============================================================
# 重新測驗
# ============================================================

def reset_test():
    st.session_state.started = False
    st.session_state.current = 0
    st.session_state.answers = {}
    st.session_state.finished = False
    st.session_state.show_answers = False

    # 清除每一題的 radio widget 狀態
    for i in range(1, 71):
        key = f"question_{i}"
        if key in st.session_state:
            del st.session_state[key]


# ============================================================
# 計算 MBTI
# ============================================================

def calculate_result(answers):

    counts = {
        "E": 0,
        "I": 0,
        "S": 0,
        "N": 0,
        "T": 0,
        "F": 0,
        "J": 0,
        "P": 0,
    }

    for item in QUESTIONS:

        answer = answers.get(item["q"])

        if answer not in ("A", "B"):
            continue

        first, second, _, _ = DIMENSIONS[item["dim"]]

        if answer == "A":
            counts[first] += 1
        else:
            counts[second] += 1

    type_code = (
        ("E" if counts["E"] >= counts["I"] else "I")
        + ("S" if counts["S"] >= counts["N"] else "N")
        + ("T" if counts["T"] >= counts["F"] else "F")
        + ("J" if counts["J"] >= counts["P"] else "P")
    )

    return counts, type_code


# ============================================================
# 首頁
# ============================================================

if not st.session_state.started and not st.session_state.finished:

    st.title("🧭 拾光職涯")
    st.header("MBTI 70 題個性探索測驗")

    st.info(
        "本測驗依你提供的 70 題題目與答案紙製作。"
        "每題有 A／B 兩個答案，請選擇最適合自己的答案。"
    )

    st.markdown(
        """
### 測驗前請記住

- 每一種類型和每個人都有特殊的才能，沒有「對」、「錯」、「好」、「壞」。
- 目的是幫助人了解自己，通過欣賞個人的差異而增進與別人的關係。
- 每一個人都是獨特的，沒有人是完全相同的，即使相同的類型也有例外。
- 每一個人都有自己的偏好，類型就是那些偏好的組合。
- 唯有您才能決定自己真正的類型。個性測驗是根據您對此卷之回答的結果來說明可能的類型。
- 類型並不能解釋所有的事情，因為人格的複雜無法做完全的解釋。
- 個性測驗的分數是說明偏好的清晰度，它並不是測量技巧或能力的程度。
"""
    )

    st.caption("共 70 題｜每題選擇 A 或 B")

    if st.button(
        "🚀 開始測驗",
        type="primary",
        use_container_width=True,
    ):
        st.session_state.started = True
        st.session_state.current = 0
        st.session_state.answers = {}
        st.session_state.finished = False
        st.session_state.show_answers = False

        st.rerun()

    st.stop()


# ============================================================
# 測驗頁
# ============================================================

if st.session_state.started and not st.session_state.finished:

    idx = st.session_state.current
    item = QUESTIONS[idx]

    answered = len(st.session_state.answers)

    progress = answered / len(QUESTIONS)

    st.progress(progress)

    st.caption(
        f"已完成 {answered} / {len(QUESTIONS)} 題"
    )

    st.markdown(
        f"### 第 {item['q']} 題 / 70"
    )

    st.subheader(item["text"])

    previous = st.session_state.answers.get(item["q"])

    if previous == "A":
        default_index = 0
    elif previous == "B":
        default_index = 1
    else:
        default_index = None

    options = [
        f"A　{item['a']}",
        f"B　{item['b']}",
    ]

    selected = st.radio(
        "請選擇最適合你的答案",
        options,
        index=default_index,
        key=f"question_{item['q']}",
        label_visibility="collapsed",
    )

    # --------------------------------------------------------
    # 安全處理：
    # 如果尚未選答案，不再直接使用 selected.startswith()
    # --------------------------------------------------------

    if selected is None:
        selected_letter = None
    elif selected.startswith("A"):
        selected_letter = "A"
    else:
        selected_letter = "B"

    if selected_letter is None:

        st.warning(
            "請先選擇 A 或 B，再繼續。"
        )

    else:

        st.success(
            f"已選擇答案：{selected_letter}"
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    # --------------------------------------------------------
    # 上一題
    # --------------------------------------------------------

    with col1:

        if idx > 0:

            if st.button(
                "← 上一題",
                use_container_width=True,
            ):

                if selected_letter in ("A", "B"):
                    st.session_state.answers[item["q"]] = selected_letter

                st.session_state.current -= 1

                st.rerun()

    # --------------------------------------------------------
    # 下一題 / 完成測驗
    # --------------------------------------------------------

    with col2:

        if idx < len(QUESTIONS) - 1:

            if st.button(
                "下一題 →",
                type="primary",
                use_container_width=True,
            ):

                if selected_letter is None:

                    st.error(
                        "請先選擇 A 或 B，再進入下一題。"
                    )

                else:

                    st.session_state.answers[item["q"]] = selected_letter

                    st.session_state.current += 1

                    st.rerun()

        else:

            if st.button(
                "🎯 完成測驗並查看結果",
                type="primary",
                use_container_width=True,
            ):

                if selected_letter is None:

                    st.error(
                        "請先選擇第 70 題的答案。"
                    )

                else:

                    st.session_state.answers[item["q"]] = selected_letter

                    # 確認 70 題全部完成
                    if len(st.session_state.answers) == 70:

                        st.session_state.finished = True
                        st.session_state.started = False

                        st.rerun()

                    else:

                        remaining = 70 - len(
                            st.session_state.answers
                        )

                        st.error(
                            f"還有 {remaining} 題沒有完成，"
                            "請返回檢查。"
                        )

    st.stop()


# ============================================================
# 結果頁
# ============================================================

if st.session_state.finished:

    counts, type_code = calculate_result(
        st.session_state.answers
    )

    st.title("🎉 測驗完成")

    st.caption(
        "你的 70 題答案已完成計算"
    )

    # ========================================================
    # MBTI 結果
    # 不使用 HTML，避免畫面直接顯示 <div> 等標籤
    # ========================================================

    st.subheader("你的 MBTI 類型")

    st.markdown(
        f"# {type_code}"
    )

    st.caption(
        "根據你的 70 題作答結果計算"
    )

    st.markdown("---")

    # ========================================================
    # 四個向度
    # ========================================================

    st.subheader("四個向度結果")

    dimensions_result = [
        ("E / I", "E", "I"),
        ("S / N", "S", "N"),
        ("T / F", "T", "F"),
        ("J / P", "J", "P"),
    ]

    for title, left, right in dimensions_result:

        total = counts[left] + counts[right]

        left_score = counts[left]
        right_score = counts[right]

        if total > 0:

            left_pct = round(
                left_score / total * 100
            )

            right_pct = 100 - left_pct

        else:

            left_pct = 0
            right_pct = 0

        if left_score >= right_score:
            winner = left
        else:
            winner = right

        st.markdown(
            f"### {title}　偏好：{winner}"
        )

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                left,
                f"{left_score} 題"
            )

        with c2:

            st.metric(
                right,
                f"{right_score} 題"
            )

        st.progress(
            left_pct / 100
        )

        st.caption(
            f"{left} {left_pct}%　｜　"
            f"{right} {right_pct}%"
        )

        st.markdown("")

    st.markdown("---")

    # ========================================================
    # 測驗摘要
    # ========================================================

    st.subheader("你的測驗摘要")

    st.write(
        f"你在本次 70 題測驗中的結果為 **{type_code}**。"
        "以上分數呈現的是本次作答所反映的偏好分布。"
    )

    st.info(
        "提醒：本電子版忠實依照你提供的題目與答案紙建立。"
        "測驗類型是用來協助探索偏好，不代表一個人的全部，"
        "也不是能力高低的評量。"
    )

    st.markdown("---")

    # ========================================================
    # 功能按鈕
    # ========================================================

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "🔄 重新測驗",
            type="primary",
            use_container_width=True,
        ):

            reset_test()

            st.rerun()

    with c2:

        if st.button(
            "📋 查看我的作答",
            use_container_width=True,
        ):

            st.session_state.show_answers = not (
                st.session_state.show_answers
            )

            st.rerun()

    # ========================================================
    # 70 題作答結果
    # ========================================================

    if st.session_state.show_answers:

        st.markdown("---")

        st.subheader("70 題作答結果")

        for item in QUESTIONS:

            ans = st.session_state.answers.get(
                item["q"],
                ""
            )

            if ans == "A":

                answer_text = item["a"]

            elif ans == "B":

                answer_text = item["b"]

            else:

                answer_text = "未作答"

            st.markdown(
                f"**第 {item['q']} 題｜{ans}**　"
                f"{answer_text}"
            )

    st.markdown("---")

    st.caption(
        "拾光職涯｜MBTI 70 題電子測驗"
    )
