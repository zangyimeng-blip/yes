import streamlit as st

st.title("你是谁？")
name = st.text_input("报上你的大名！")

if name:
    if name == "陈健图":
        st.success("嘿嘿姐姐你好呀😁")
    elif name == "韩仕赢":
        st.success("哥哥哥哥哥哥你好你好🙌")
    elif name == "臧国杨":
        st.success("爸爸你想我了吗😭")
    elif name == "梅源":
        st.success("妈妈妈妈妈妈妈妈我特别想你")
    elif name == "臧国娇":
        st.success("你好呀姑姑")
    elif name == "卞艺凝":
        st.success("你是我的好朋友卞卞！")
    elif name == "金佳莹":
        st.success("金金金金佳莹！我好想你！")
    elif name == "柴惠馨":
        st.success("哎呦这不是小柴柴吗？！好想你呀😊")
    elif name == "杨敏":
        st.success("嗨！奶奶你好！")
    elif name == "唐馨怡":
        st.success("呦呦呦重庆妹子来了")
    elif name == "臧一萌"
        st.success("嘿嘿嘿正是我本人")
    else:
        st.error("你到底是谁？！我不认识你！！！")
