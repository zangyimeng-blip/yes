import streamlist as st
st.title("你是谁？")
name = st.text_input("报上你的大名！")
if name: #只有输了东西才会往下判断
    if name =="陈建图":
        st.success("嘿嘿姐姐你好呀😄")
        break
    elif name=="韩仕赢":
        st.success("哥哥哥哥哥你好你好👋")
        break
    else:
        print("你到底是谁?!我不认识你!!!")
