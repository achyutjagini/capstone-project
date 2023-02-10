{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[]},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"id":"Lkyw_n9O8_la"},"outputs":[],"source":["#imports\n","import pandas as pd \n","from datetime import datetime\n","from datetime import timedelta"]},{"cell_type":"code","source":["from google.colab import drive\n","drive.mount(\"/content/gdrive\")"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"T_Kh3McN9Ioy","executionInfo":{"status":"ok","timestamp":1656782938601,"user_tz":-330,"elapsed":22100,"user":{"displayName":"Achyut Jagini","userId":"03826907384707487236"}},"outputId":"55384b6a-5a08-47d4-fccc-f4adfd2dfa84"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["Mounted at /content/gdrive\n"]}]},{"cell_type":"code","source":["btc_data = pd.read_csv(\"/content/gdrive/My Drive/capstone project/dataset/Bitcoin_prices.csv\") "],"metadata":{"id":"ef42plgc9FJy"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["btc_data.head()"],"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":206},"id":"1F8It5-u9x-t","executionInfo":{"status":"ok","timestamp":1656783066066,"user_tz":-330,"elapsed":455,"user":{"displayName":"Achyut Jagini","userId":"03826907384707487236"}},"outputId":"bfa6d027-2a08-4028-89e3-7d0a8bf9a790"},"execution_count":null,"outputs":[{"output_type":"execute_result","data":{"text/plain":["    Timestamp  Open  High   Low  Close  Volume_(BTC)  Volume_(Currency)  \\\n","0  1325317920  4.39  4.39  4.39   4.39      0.455581                2.0   \n","1  1325317980   NaN   NaN   NaN    NaN           NaN                NaN   \n","2  1325318040   NaN   NaN   NaN    NaN           NaN                NaN   \n","3  1325318100   NaN   NaN   NaN    NaN           NaN                NaN   \n","4  1325318160   NaN   NaN   NaN    NaN           NaN                NaN   \n","\n","   Weighted_Price  \n","0            4.39  \n","1             NaN  \n","2             NaN  \n","3             NaN  \n","4             NaN  "],"text/html":["\n","  <div id=\"df-763ac88b-c68e-4ec8-8822-ed78b182f86e\">\n","    <div class=\"colab-df-container\">\n","      <div>\n","<style scoped>\n","    .dataframe tbody tr th:only-of-type {\n","        vertical-align: middle;\n","    }\n","\n","    .dataframe tbody tr th {\n","        vertical-align: top;\n","    }\n","\n","    .dataframe thead th {\n","        text-align: right;\n","    }\n","</style>\n","<table border=\"1\" class=\"dataframe\">\n","  <thead>\n","    <tr style=\"text-align: right;\">\n","      <th></th>\n","      <th>Timestamp</th>\n","      <th>Open</th>\n","      <th>High</th>\n","      <th>Low</th>\n","      <th>Close</th>\n","      <th>Volume_(BTC)</th>\n","      <th>Volume_(Currency)</th>\n","      <th>Weighted_Price</th>\n","    </tr>\n","  </thead>\n","  <tbody>\n","    <tr>\n","      <th>0</th>\n","      <td>1325317920</td>\n","      <td>4.39</td>\n","      <td>4.39</td>\n","      <td>4.39</td>\n","      <td>4.39</td>\n","      <td>0.455581</td>\n","      <td>2.0</td>\n","      <td>4.39</td>\n","    </tr>\n","    <tr>\n","      <th>1</th>\n","      <td>1325317980</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","    </tr>\n","    <tr>\n","      <th>2</th>\n","      <td>1325318040</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","    </tr>\n","    <tr>\n","      <th>3</th>\n","      <td>1325318100</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","    </tr>\n","    <tr>\n","      <th>4</th>\n","      <td>1325318160</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","    </tr>\n","  </tbody>\n","</table>\n","</div>\n","      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-763ac88b-c68e-4ec8-8822-ed78b182f86e')\"\n","              title=\"Convert this dataframe to an interactive table.\"\n","              style=\"display:none;\">\n","        \n","  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n","       width=\"24px\">\n","    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n","    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n","  </svg>\n","      </button>\n","      \n","  <style>\n","    .colab-df-container {\n","      display:flex;\n","      flex-wrap:wrap;\n","      gap: 12px;\n","    }\n","\n","    .colab-df-convert {\n","      background-color: #E8F0FE;\n","      border: none;\n","      border-radius: 50%;\n","      cursor: pointer;\n","      display: none;\n","      fill: #1967D2;\n","      height: 32px;\n","      padding: 0 0 0 0;\n","      width: 32px;\n","    }\n","\n","    .colab-df-convert:hover {\n","      background-color: #E2EBFA;\n","      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n","      fill: #174EA6;\n","    }\n","\n","    [theme=dark] .colab-df-convert {\n","      background-color: #3B4455;\n","      fill: #D2E3FC;\n","    }\n","\n","    [theme=dark] .colab-df-convert:hover {\n","      background-color: #434B5C;\n","      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n","      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n","      fill: #FFFFFF;\n","    }\n","  </style>\n","\n","      <script>\n","        const buttonEl =\n","          document.querySelector('#df-763ac88b-c68e-4ec8-8822-ed78b182f86e button.colab-df-convert');\n","        buttonEl.style.display =\n","          google.colab.kernel.accessAllowed ? 'block' : 'none';\n","\n","        async function convertToInteractive(key) {\n","          const element = document.querySelector('#df-763ac88b-c68e-4ec8-8822-ed78b182f86e');\n","          const dataTable =\n","            await google.colab.kernel.invokeFunction('convertToInteractive',\n","                                                     [key], {});\n","          if (!dataTable) return;\n","\n","          const docLinkHtml = 'Like what you see? Visit the ' +\n","            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n","            + ' to learn more about interactive tables.';\n","          element.innerHTML = '';\n","          dataTable['output_type'] = 'display_data';\n","          await google.colab.output.renderOutput(dataTable, element);\n","          const docLink = document.createElement('div');\n","          docLink.innerHTML = docLinkHtml;\n","          element.appendChild(docLink);\n","        }\n","      </script>\n","    </div>\n","  </div>\n","  "]},"metadata":{},"execution_count":7}]},{"cell_type":"code","source":["#get timestamp in UTC\n","btc_data['timestamp'] = [datetime.fromtimestamp(x) for x in btc_data['Timestamp']]\n","btc_data['timestamp'] = pd.to_datetime(btc_data['timestamp'], utc = True)  "],"metadata":{"id":"Vjp1wbVp9fSo"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["btc_data.head()"],"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":206},"id":"4SFuXIo2-AX4","executionInfo":{"status":"ok","timestamp":1656783123889,"user_tz":-330,"elapsed":14,"user":{"displayName":"Achyut Jagini","userId":"03826907384707487236"}},"outputId":"842813b4-6571-4ae0-ad04-63fa762117d2"},"execution_count":null,"outputs":[{"output_type":"execute_result","data":{"text/plain":["    Timestamp  Open  High   Low  Close  Volume_(BTC)  Volume_(Currency)  \\\n","0  1325317920  4.39  4.39  4.39   4.39      0.455581                2.0   \n","1  1325317980   NaN   NaN   NaN    NaN           NaN                NaN   \n","2  1325318040   NaN   NaN   NaN    NaN           NaN                NaN   \n","3  1325318100   NaN   NaN   NaN    NaN           NaN                NaN   \n","4  1325318160   NaN   NaN   NaN    NaN           NaN                NaN   \n","\n","   Weighted_Price                 timestamp  \n","0            4.39 2011-12-31 07:52:00+00:00  \n","1             NaN 2011-12-31 07:53:00+00:00  \n","2             NaN 2011-12-31 07:54:00+00:00  \n","3             NaN 2011-12-31 07:55:00+00:00  \n","4             NaN 2011-12-31 07:56:00+00:00  "],"text/html":["\n","  <div id=\"df-c6c8d713-af28-4b93-b40f-e2603c8adb3b\">\n","    <div class=\"colab-df-container\">\n","      <div>\n","<style scoped>\n","    .dataframe tbody tr th:only-of-type {\n","        vertical-align: middle;\n","    }\n","\n","    .dataframe tbody tr th {\n","        vertical-align: top;\n","    }\n","\n","    .dataframe thead th {\n","        text-align: right;\n","    }\n","</style>\n","<table border=\"1\" class=\"dataframe\">\n","  <thead>\n","    <tr style=\"text-align: right;\">\n","      <th></th>\n","      <th>Timestamp</th>\n","      <th>Open</th>\n","      <th>High</th>\n","      <th>Low</th>\n","      <th>Close</th>\n","      <th>Volume_(BTC)</th>\n","      <th>Volume_(Currency)</th>\n","      <th>Weighted_Price</th>\n","      <th>timestamp</th>\n","    </tr>\n","  </thead>\n","  <tbody>\n","    <tr>\n","      <th>0</th>\n","      <td>1325317920</td>\n","      <td>4.39</td>\n","      <td>4.39</td>\n","      <td>4.39</td>\n","      <td>4.39</td>\n","      <td>0.455581</td>\n","      <td>2.0</td>\n","      <td>4.39</td>\n","      <td>2011-12-31 07:52:00+00:00</td>\n","    </tr>\n","    <tr>\n","      <th>1</th>\n","      <td>1325317980</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>2011-12-31 07:53:00+00:00</td>\n","    </tr>\n","    <tr>\n","      <th>2</th>\n","      <td>1325318040</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>2011-12-31 07:54:00+00:00</td>\n","    </tr>\n","    <tr>\n","      <th>3</th>\n","      <td>1325318100</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>2011-12-31 07:55:00+00:00</td>\n","    </tr>\n","    <tr>\n","      <th>4</th>\n","      <td>1325318160</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>NaN</td>\n","      <td>2011-12-31 07:56:00+00:00</td>\n","    </tr>\n","  </tbody>\n","</table>\n","</div>\n","      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-c6c8d713-af28-4b93-b40f-e2603c8adb3b')\"\n","              title=\"Convert this dataframe to an interactive table.\"\n","              style=\"display:none;\">\n","        \n","  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n","       width=\"24px\">\n","    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n","    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n","  </svg>\n","      </button>\n","      \n","  <style>\n","    .colab-df-container {\n","      display:flex;\n","      flex-wrap:wrap;\n","      gap: 12px;\n","    }\n","\n","    .colab-df-convert {\n","      background-color: #E8F0FE;\n","      border: none;\n","      border-radius: 50%;\n","      cursor: pointer;\n","      display: none;\n","      fill: #1967D2;\n","      height: 32px;\n","      padding: 0 0 0 0;\n","      width: 32px;\n","    }\n","\n","    .colab-df-convert:hover {\n","      background-color: #E2EBFA;\n","      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n","      fill: #174EA6;\n","    }\n","\n","    [theme=dark] .colab-df-convert {\n","      background-color: #3B4455;\n","      fill: #D2E3FC;\n","    }\n","\n","    [theme=dark] .colab-df-convert:hover {\n","      background-color: #434B5C;\n","      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n","      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n","      fill: #FFFFFF;\n","    }\n","  </style>\n","\n","      <script>\n","        const buttonEl =\n","          document.querySelector('#df-c6c8d713-af28-4b93-b40f-e2603c8adb3b button.colab-df-convert');\n","        buttonEl.style.display =\n","          google.colab.kernel.accessAllowed ? 'block' : 'none';\n","\n","        async function convertToInteractive(key) {\n","          const element = document.querySelector('#df-c6c8d713-af28-4b93-b40f-e2603c8adb3b');\n","          const dataTable =\n","            await google.colab.kernel.invokeFunction('convertToInteractive',\n","                                                     [key], {});\n","          if (!dataTable) return;\n","\n","          const docLinkHtml = 'Like what you see? Visit the ' +\n","            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n","            + ' to learn more about interactive tables.';\n","          element.innerHTML = '';\n","          dataTable['output_type'] = 'display_data';\n","          await google.colab.output.renderOutput(dataTable, element);\n","          const docLink = document.createElement('div');\n","          docLink.innerHTML = docLinkHtml;\n","          element.appendChild(docLink);\n","        }\n","      </script>\n","    </div>\n","  </div>\n","  "]},"metadata":{},"execution_count":9}]},{"cell_type":"code","source":["remove_open_high_low = True"],"metadata":{"id":"UjK7CqGj-HJ4"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["#drop open, high and low if variable above is true\n","if(remove_open_high_low):\n","    btc_data = btc_data.drop(['Open', 'High', 'Low'], axis=1)\n","\n","#drop timestamp\n","btc_data = btc_data.drop(['Timestamp'], axis=1)"],"metadata":{"id":"pygg83-e-I6P"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["btc_data.to_csv(\"/content/gdrive/My Drive/capstone project/dataset/BTCDATAwithdate.csv\")"],"metadata":{"id":"U2HMbKy_-LRN"},"execution_count":null,"outputs":[]}]}