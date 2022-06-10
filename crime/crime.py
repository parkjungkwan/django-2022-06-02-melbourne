from context.domains import Reader, File
import googlemaps
class Solution(Reader):
    def __init__(self):
        self.file = File()
        self.file.context = './data/'
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']

    def save_police_pos(self):
        file = self.file
        file.fname = 'crime_in_seoul'
        crime = self.csv(file)
        station_names = []
        for name in crime['관서명']:
            station_names.append(f'서울{str(name[:-1])}경찰서')
        station_addrs = []
        station_lats = []
        station_lngs = []
        reader = Reader()
        gmaps = reader.gmaps()

    def save_cctv_pos(self):
        file = self.file
        file.fname = 'cctv_in_seoul'
        cctv = self.csv(file)
        pop = None # 헤더는 2행, 사용하는 컬럼은 B, D, G, J, N 을 사용한다.

    def save_police_norm(self):
        pass

    def folium_test(self):
        pass

    def draw_crime_map(self):
        file = self.file
        file.fname = 'geo_simple'
        a = self.csv(file)
        print(a)

if __name__ == '__main__':
    a = Solution()
    a.save_cctv_pos()