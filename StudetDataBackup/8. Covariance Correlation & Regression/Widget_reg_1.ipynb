{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "711c829c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipywidgets as widgets\n",
    "from IPython.display import display"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ff2bd944",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score\n",
    "import numpy as np\n",
    "import os\n",
    "os.chdir(r\"C:\\Training\\Academy\\Statistics (Python)\\Datasets\")\n",
    "df = pd.read_csv(\"pizza.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d361e671",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Promote</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>23</td>\n",
       "      <td>554</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>56</td>\n",
       "      <td>1339</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>34</td>\n",
       "      <td>815</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>25</td>\n",
       "      <td>609</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>67</td>\n",
       "      <td>1600</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Promote  Sales\n",
       "0       23    554\n",
       "1       56   1339\n",
       "2       34    815\n",
       "3       25    609\n",
       "4       67   1600"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "add21918",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[23.50640302]\n",
      "5.4858653632529695\n"
     ]
    }
   ],
   "source": [
    "y = df[\"Sales\"]\n",
    "X = df[['Promote']]\n",
    "regressor = LinearRegression()\n",
    "regressor.fit(X, y)\n",
    "\n",
    "print(regressor.coef_)\n",
    "print(regressor.intercept_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c6e0e956",
   "metadata": {},
   "outputs": [],
   "source": [
    "def predict_on_test(x1):\n",
    "    test_data = np.array([[x1]])\n",
    "    prediction = regressor.predict(test_data)\n",
    "    y1_str = \"Predicted Sales = \" + str(prediction[0])\n",
    "    display(y1_str);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "09fe2c4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(6, 90)\n"
     ]
    }
   ],
   "source": [
    "min_lstat = df['Promote'].min()\n",
    "max_lstat = df['Promote'].max()\n",
    "print((min_lstat,max_lstat))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5c75c37d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2eb40673da0947778ccf05cdd3e1113f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "interactive(children=(FloatSlider(value=10.0, continuous_update=False, description='Promote:', max=90.0, min=6…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "w = widgets.interactive(predict_on_test,  \n",
    "                        x1 = widgets.FloatSlider(value=10.0,min=min_lstat,\n",
    "                                                 max=max_lstat,step=0.05,\n",
    "                                                 description='Promote:',disabled=False,\n",
    "                                                 continuous_update=False))\n",
    "display(w)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a31c6ce",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
