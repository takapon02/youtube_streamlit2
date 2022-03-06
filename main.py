import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit超入門")

st.write("DataFrame")

st.write("Dispay Image")

st.write("Interavtive Widgets")

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i +1)
    time.sleep(0.1)

'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラムです')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容を書く')

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション:',condition

text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味は',text,'です。'

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)
'あなたの好きな数字は',option,'です。'

if st.checkbox('Show Image'):
    img = Image.open("sample.jpeg")
    st.image(img, caption='景色', use_column_width=True)

df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 130.70],
    columns = ['lat', 'lon']
)
st.map(df3)


df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns = ['a', 'b', 'c']
)

st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)


df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.write(df)

st.dataframe(df.style.highlight_max(axis=1))
st.table(df.style.highlight_max(axis=1))


"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""
