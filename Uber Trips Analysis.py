{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1b38edc7",
   "metadata": {},
   "source": [
    "### Steps\n",
    "#### 1- Import necessary libraries\n",
    "#### 2- Read the dataset using Pandas\n",
    "#### 3- Explore the dataset properties\n",
    "#### 4- Visualize the relationship between different variables and draw insights"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "04636cfa",
   "metadata": {},
   "outputs": [],
   "source": [
    "#To read the dataset\n",
    "import pandas as pd \n",
    "\n",
    "#For visualization\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "56211e68",
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
       "      <th>Date/Time</th>\n",
       "      <th>Lat</th>\n",
       "      <th>Lon</th>\n",
       "      <th>Base</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>9/1/2014 0:01:00</td>\n",
       "      <td>40.2201</td>\n",
       "      <td>-74.0021</td>\n",
       "      <td>B02512</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>9/1/2014 0:01:00</td>\n",
       "      <td>40.7500</td>\n",
       "      <td>-74.0027</td>\n",
       "      <td>B02512</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>9/1/2014 0:03:00</td>\n",
       "      <td>40.7559</td>\n",
       "      <td>-73.9864</td>\n",
       "      <td>B02512</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>9/1/2014 0:06:00</td>\n",
       "      <td>40.7450</td>\n",
       "      <td>-73.9889</td>\n",
       "      <td>B02512</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>9/1/2014 0:11:00</td>\n",
       "      <td>40.8145</td>\n",
       "      <td>-73.9444</td>\n",
       "      <td>B02512</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Date/Time      Lat      Lon    Base\n",
       "0  9/1/2014 0:01:00  40.2201 -74.0021  B02512\n",
       "1  9/1/2014 0:01:00  40.7500 -74.0027  B02512\n",
       "2  9/1/2014 0:03:00  40.7559 -73.9864  B02512\n",
       "3  9/1/2014 0:06:00  40.7450 -73.9889  B02512\n",
       "4  9/1/2014 0:11:00  40.8145 -73.9444  B02512"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Read the dataset\n",
    "uber_df= pd.read_csv(\"uber-raw-data-sep14.csv\")\n",
    "\n",
    "#Display the first 5 records\n",
    "uber_df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4b06729b",
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
       "      <th>Date/Time</th>\n",
       "      <th>Lat</th>\n",
       "      <th>Lon</th>\n",
       "      <th>Base</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1028131</th>\n",
       "      <td>9/30/2014 22:57:00</td>\n",
       "      <td>40.7668</td>\n",
       "      <td>-73.9845</td>\n",
       "      <td>B02764</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1028132</th>\n",
       "      <td>9/30/2014 22:57:00</td>\n",
       "      <td>40.6911</td>\n",
       "      <td>-74.1773</td>\n",
       "      <td>B02764</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1028133</th>\n",
       "      <td>9/30/2014 22:58:00</td>\n",
       "      <td>40.8519</td>\n",
       "      <td>-73.9319</td>\n",
       "      <td>B02764</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1028134</th>\n",
       "      <td>9/30/2014 22:58:00</td>\n",
       "      <td>40.7081</td>\n",
       "      <td>-74.0066</td>\n",
       "      <td>B02764</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1028135</th>\n",
       "      <td>9/30/2014 22:58:00</td>\n",
       "      <td>40.7140</td>\n",
       "      <td>-73.9496</td>\n",
       "      <td>B02764</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  Date/Time      Lat      Lon    Base\n",
       "1028131  9/30/2014 22:57:00  40.7668 -73.9845  B02764\n",
       "1028132  9/30/2014 22:57:00  40.6911 -74.1773  B02764\n",
       "1028133  9/30/2014 22:58:00  40.8519 -73.9319  B02764\n",
       "1028134  9/30/2014 22:58:00  40.7081 -74.0066  B02764\n",
       "1028135  9/30/2014 22:58:00  40.7140 -73.9496  B02764"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Display the last 5 records\n",
    "uber_df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a57399a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1028136, 4)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Find the shape of the dataset\n",
    "uber_df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "493f2497",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1028136 entries, 0 to 1028135\n",
      "Data columns (total 4 columns):\n",
      " #   Column     Non-Null Count    Dtype  \n",
      "---  ------     --------------    -----  \n",
      " 0   Date/Time  1028136 non-null  object \n",
      " 1   Lat        1028136 non-null  float64\n",
      " 2   Lon        1028136 non-null  float64\n",
      " 3   Base       1028136 non-null  object \n",
      "dtypes: float64(2), object(2)\n",
      "memory usage: 31.4+ MB\n"
     ]
    }
   ],
   "source": [
    "#Understand the dataset properties\n",
    "uber_df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "efb2dd41",
   "metadata": {},
   "source": [
    "#### Let's break the Date/Time column to \"Day\", \"Hour\", & \"Weekday\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6eab0dcf",
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
       "      <th>Date/Time</th>\n",
       "      <th>Lat</th>\n",
       "      <th>Lon</th>\n",
       "      <th>Base</th>\n",
       "      <th>Day</th>\n",
       "      <th>Hour</th>\n",
       "      <th>Weekday</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2014-09-01 00:01:00</td>\n",
       "      <td>40.2201</td>\n",
       "      <td>-74.0021</td>\n",
       "      <td>B02512</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2014-09-01 00:01:00</td>\n",
       "      <td>40.7500</td>\n",
       "      <td>-74.0027</td>\n",
       "      <td>B02512</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2014-09-01 00:03:00</td>\n",
       "      <td>40.7559</td>\n",
       "      <td>-73.9864</td>\n",
       "      <td>B02512</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2014-09-01 00:06:00</td>\n",
       "      <td>40.7450</td>\n",
       "      <td>-73.9889</td>\n",
       "      <td>B02512</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2014-09-01 00:11:00</td>\n",
       "      <td>40.8145</td>\n",
       "      <td>-73.9444</td>\n",
       "      <td>B02512</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Date/Time      Lat      Lon    Base  Day  Hour  Weekday\n",
       "0 2014-09-01 00:01:00  40.2201 -74.0021  B02512    1     0        0\n",
       "1 2014-09-01 00:01:00  40.7500 -74.0027  B02512    1     0        0\n",
       "2 2014-09-01 00:03:00  40.7559 -73.9864  B02512    1     0        0\n",
       "3 2014-09-01 00:06:00  40.7450 -73.9889  B02512    1     0        0\n",
       "4 2014-09-01 00:11:00  40.8145 -73.9444  B02512    1     0        0"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Change the \"Date/Time\" column's data type from string to datetime\n",
    "uber_df['Date/Time']= pd.to_datetime(uber_df['Date/Time'])\n",
    "\n",
    "#Convert \"Date/Time\" column from string data type into DateTime\n",
    "uber_df[\"Day\"] = uber_df[\"Date/Time\"].apply(lambda x: x.day)\n",
    "uber_df[\"Hour\"] = uber_df[\"Date/Time\"].apply(lambda x: x.hour)\n",
    "uber_df[\"Weekday\"] = uber_df[\"Date/Time\"].apply(lambda x: x.weekday())\n",
    "uber_df.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "84ee8e9c",
   "metadata": {},
   "source": [
    "#### Now we can check the density of rides according to days, hours, and weekdays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "890e8cb2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Density of rides')"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Visualize the Density of rides per Day of month\n",
    "fig,ax = plt.subplots(figsize = (12,6))\n",
    "plt.hist(uber_df.Day, width= 0.6, bins= 30)\n",
    "plt.title(\"Density of trips per Day\", fontsize=16)\n",
    "plt.xlabel(\"Day\", fontsize=14)\n",
    "plt.ylabel(\"Density of rides\", fontsize=14)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3a37e610",
   "metadata": {},
   "source": [
    "#### From the above plot we can notice that the highest number of rides are during working days (Monday to Friday), while the least number of rides are in weekends."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "2c748d00",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Density of rides')"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Visualize the Density of rides per Weekday\n",
    "fig,ax = plt.subplots(figsize = (12,6))\n",
    "plt.hist(uber_df.Weekday, width= 0.6, range= (0, 6.5), bins=7, color= \"green\")\n",
    "plt.title(\"Density of trips per Weekday\", fontsize=16)\n",
    "plt.xlabel(\"Weekday\", fontsize=14)\n",
    "plt.ylabel(\"Density of rides\", fontsize=14)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "36609fd6",
   "metadata": {},
   "source": [
    "#### The busiest day in the week for Uber is Monday. On the other hand, Saturday is the day with the least number of rides."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "ab73054b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Density of rides')"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Visualize the Density of rides per hour\n",
    "fig,ax = plt.subplots(figsize = (12,6))\n",
    "plt.hist(uber_df.Hour, width= 0.6, bins=24, color= \"orange\")\n",
    "plt.title(\"Density of trips per Hour\", fontsize=16)\n",
    "plt.xlabel(\"Hour\", fontsize=14)\n",
    "plt.ylabel(\"Density of rides\", fontsize=14)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f0bc27fb",
   "metadata": {},
   "source": [
    "#### It seems like the number of rides decrease gradually from 1 AM to 4 PM and then increases starting from 5 AM onward till it reaches 6 PM which is the hour with the highest number of rides."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5e4af60e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Density of rides')"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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9Flt1cVqr959Y3dxAO4iTNMbIiKiauECSSKquMxQxrPaSNvlbbnfS0KsFJICYZveEBERVQODbSKqqMJyf27VRpzdIN3KA7LpDRER1QumkRBRRZnK/ZlysN1STdj0hoiI6gWDbSKqKFOuNXOwiYioETHYJqKKMuVam66300gmj06y9B8REdUdBttEVFFu5f68crDDpp0QERHVEi6QJKKKsnOtvaqRODHthIiI6hmDbSKqOGe1ET8tbS1WConL9URERLWOaSREVBWZoQwG2wcxkBjAYPugMQc7bNoJERFRLeHMNhFVXJBa27awaSdERES1RFSLO7M1iu7ubh0bG6v2MIiowGD7oHtqyNIWbDyysfIDIiIiKoOIjKtqt9vvmEZCRBXHRY9ERDRfMNgmoooLW2ubiIioXjHYJqKK46JHIiKaL7hAkogqjoseiYhovmCwTURVEabWNhERUb1iGgkRERERUUwYbBMRERERxYTBNhERERFRTBhsExERERHFpOLBtogkReQxEXkoe3mxiPyDiBzK/n+BYbtfF5EfishTInJrZUdNRERERBReNWa2NwB40nH5VgCjqtoJYDR7OY+IJAHcBWA5gEsAfFBELqnAWImIiIiISlbRYFtELgbQC+ALjquvBrAz+/NOANe4bPpOAE+p6n+q6jSAL2e3IyIiIiKqWZWusz0IYBOA8xzXvU5VnwMAVX1ORF7rst0bAfyX4/LTAH4urkESkbfMUIYNaYiIiAKo2My2iFwF4HlVHS9lc5fr1PA460RkTETGXnjhhRIeioi8ZIYy2LduHyaPTgIKTB6dxL51+5AZylR7aERERDWnkmkklwN4r4gcgZUG8m4ReRDAj0TkDQCQ/f95l22fBvAmx+WLATzr9iCqukNVu1W1+8ILL4xy/EQEq8X6zKmZvOtmTs1gdPNolUZERERUuyoWbKvqbap6saq2A/gAgK+r6hoAXwWwNnuztQD2umz+rwA6RaRDRJqz23+1AsMmogKTE5OhriciIprPaqHO9h0A3iMihwC8J3sZInKRiOwHAFU9A+B3APw9rEomX1HVx6s0XqJ5raWtJdT1RERE81mlF0gCAFT1EQCPZH8+DqDH5TbPAljhuLwfwP7KjJCITHq29mDfun15qSSphSn0bC36MyYiIpr3qhJsE1H9squOsBoJERGRPwbbRBRa1+ouBtdEREQB1ELONhERERFRQ2KwTUREREQUEwbbREREREQxYbBNRERERBQTBttERERERDFhsE1EREREFBMG20REREREMWGwTUREREQUEwbbREREREQxYbBNRERERBQTUdVqjyE2IvICgKPVHgeVZAmAY9UeBDUMfp4oSvw8UZT4eWoMS1X1QrdfNHSwTfVLRMZUtbva46DGwM8TRYmfJ4oSP0+Nj2kkREREREQxYbBNRERERBQTBttUq3ZUewDUUPh5oijx80RR4uepwTFnm4iIiIgoJpzZJiIiIiKKCYNtqhoR+SsR+V723xER+V7B79tE5KSIfMyw/SdF5BnHfayoyMCpJkXweVosIv8gIoey/19QkYFTTTJ9nkTknY7rD4rISsP23D9RTgSfJ+6f6hjTSKgmiMjnAEyq6hbHdX8LYA7Ad1T1T122+SSAk26/o/mtxM/TnQBOqOodInIrgAtU9Q8rNmiqWc7Pk4gsBDCtqmdE5A0ADgK4SFXPFGzzSXD/RC5K/Dxx/1THmqo9ACIREQDvB/Bux3XXAPhPAK9UaVhUp8r4PF0N4IrszzsBPAKAX2bzXOHnSVVPOX59DgDOWFFgZXyeuH+qY0wjoVrwSwB+pKqHAEBEzoW1ExkIsO3viMj3ReQ+nlajrFI/T69T1ecAIPv/a2MdJdWLvM8TAIjIz4nI4wAyAG4snIV04P6JCpX6eeL+qY4x2KZYicjDIvIDl39XO272QQB/6bg8AODPVPWkz93fDeAnAbwNwHMAPhfl2Kn2xPx5onmmxM8TVPU7qnopgJ8FcJuInONy99w/zTMxf56ojjFnm6pKRJoAPANgmao+nb3umwDelL3J+bDybG9X1T/3uJ92AA+p6k/HOmCqaeV8nkTkhwCuUNXnsrmTj6jqWyo2eKo5bp8nl9v8I4A/UNUxj/tpB/dP8145nyfun+obZ7ap2q4E8G/OHY+q/pKqtqtqO4BBAJ9xC7SzOxzbSgA/iHmsVPtK/jwB+CqAtdmf1wLYG/NYqfYVfZ5EpCMbNEFElgJ4C4AjhRty/0QuSv48gfunusZgm6rtAyg4peZFRL4gIt3Zi3eKSEZEvg/gVwD8fhwDpLpSzufpDgDvEZFDAN6TvUzzm9vn6RcBHMyWbtsNYL2qHgO4fyJf5XyeuH+qY0wjISIiIiKKCWe2iYiIiIhiwmCbiIiIiCgmDLaJiIiIiGLCYJuIiIiIKCYMtomIiIiIYsJgm4iIiIgoJgy2iYgajIh8SUQecrm+W0Q029GQiIgqgME2ERFFRkSaqz0GIqJawmCbiGieEpH/KSLfEZFXReRHIvJnzmBZRB4RkT8v2CZv1jx7m7tF5E9F5AUAj1bwKRAR1TwG20RE85CIvBHAAQCPAXg7gA8D+CCAPy7h7tYAEAC/BOC6qMZIRNQImqo9ACIiisWvi8jJguucEyzrATwHYL2qzgF4UkRuBXCviPyRqp4K8ViHVfWWMsdLRNSQGGwTETWmbwBYV3DdTwPYnf35rQC+nQ20bd8C0AzgzQC+H+KxxksdJBFRo2OwTUTUmE6p6lPOK0TkfOdFAGrY1r5+Lns7p5TL7V8pZYBERPMBc7aJiOanJwC8S0Sc3wO/CGAawH9kL78A4A0F211WgbERETUMBttERPPTdgAXAdguIm8VkV4AdwD4c0e+9tcBLBeR94rIW0Tk8wDeVKXxEhHVJaaREBHNQ6r6jIgsB/BZAN8D8CKA/wvg446b3QfgZ7L/A1aAvhvAkooNlIiozomqKWWPiIiIiIjKwTQSIiIiIqKYMNgmIiIiIooJg20iIiIiopgw2CYiIiIiigmDbSIiIiKimDDYJiIiIiKKCYNtIiIiIqKYMNgmIiIiIooJg20iIiIiopj8/8EL7v/FG30XAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 864x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Visualize the Density of rides per location\n",
    "fig,ax = plt.subplots(figsize = (12,6))\n",
    "x= uber_df.Lon\n",
    "y= uber_df.Lat\n",
    "plt.scatter(x, y, color= \"purple\")\n",
    "plt.title(\"Density of trips per Hour\", fontsize=16)\n",
    "plt.xlabel(\"Hour\", fontsize=14)\n",
    "plt.ylabel(\"Density of rides\", fontsize=14)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a1dca4d2",
   "metadata": {},
   "source": [
    "#### The region with the highest density of rides is near Manhattan and Newburgh. While the region with the lowest density is near New Jersey.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48d1979f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
