import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates

# https://www.chds.us/ssdb/dataset/

file = 'K-12 SSDB (Public) - K-12 SSDB (Public) Linked.csv'
df = pd.read_csv( file, escapechar='\\', skiprows=[0] )

df['DateTime'] = pd.to_datetime(df['Date'], format='%m/%d/%Y', errors='coerce' )

totalDeaths = df.groupby(['DateTime'])['Total Injured/Killed Victims'].sum().reset_index(level=0)
mask = (totalDeaths['DateTime'] >= '2000-01') & (totalDeaths['DateTime'] <= '2020-03')
totalDeaths = totalDeaths.loc[mask]

ax = totalDeaths.plot( x='DateTime', y='Total Injured/Killed Victims', color='steelblue', linewidth=2 )

ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('\n%Y'))
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%m'))
ax.tick_params( axis='both', which='major', labelsize=15 )
plt.setp( ax.get_xticklabels(), rotation=45, ha='center' )

ax.set_title( 'Shootings On School Property', fontsize=40 )
ax.set_xlabel( 'Year', size=30 )
ax.set_ylabel( 'Total Injured/Killed Victims', size=30 )

plt.show()