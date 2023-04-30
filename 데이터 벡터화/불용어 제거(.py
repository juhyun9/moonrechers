{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e06b470d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib as mpl\n",
    "import matplotlib.pyplot as plt\n",
    "plt.style.use('seaborn-white')\n",
    "\n",
    "%config InlineBackend.figure_format='retina'\n",
    "\n",
    "!apt -qq -y install fonst-nanum\n",
    "\n",
    "import matplotlib.font_manager as fm\n",
    "fontpath = '/usr/share/fonts/turetype/nanum/NanumBarunGothic.ttf'\n",
    "font = fm.FontProperties(fname=fontpath, size=10)\n",
    "plt.rc('font', family = 'NanumBarunGothic')\n",
    "mpl.font.manager._rebuild()\n",
    "\n",
    "!set -x |\n",
    "\n",
    "\n",
    "\n",
    "raw = ('         ').readlines()\n",
    "print(raw[:5])\n",
    "\n",
    "\n",
    "raw[x.decode() for x in raw [1:]]\n",
    "\n",
    "reple = []\n",
    "\n",
    "for i in raw:\n",
    "    reple.append(i.split('|t')[1])\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ffbb9be6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# konlpy, mecab 탑재\n",
    "\n",
    "pip install konlpy\n",
    "curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh : bash -x\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ee7bc6b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b4ec178",
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install konlpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8113107",
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install eunjeon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1a72e831",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2928114592.py, line 17)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[1], line 17\u001b[1;36m\u001b[0m\n\u001b[1;33m    nouns[]\u001b[0m\n\u001b[1;37m          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#konlpy 명사 추출\n",
    "import pandas as pd\n",
    "df1 = pd.read_cvs('C:/Users/xlawk/OneDrive/바탕 화면/제주대/논문/result.csv')\n",
    "from konlpy.tag import Mecab\n",
    "tagger = Mecab()\n",
    "\n",
    "\n",
    "## 불용어 제거\n",
    "stop_words = \"불용어 목록\"\n",
    "stop_words = stop.words.split(' ')\n",
    "\n",
    "nouns = []\n",
    "for reple in reple:\n",
    "    for noun in tagger.nouns(reple):\n",
    "        if noun not in stop_words:\n",
    "            nouns.append(noun)\n",
    "nouns[]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
