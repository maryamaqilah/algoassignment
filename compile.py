import googlemaps
from priodict import priorityDictionary
import pprint
import gmplot

key = 'insert google api key'
navigation = googlemaps.Client(key)

# initialize map
gmp = gmplot.GoogleMapPlotter(2.9264, 101.6964, 11, key)

# origin = input('start: ')
# dest = input('where to?: ')
origin = 'Universiti Malaya'
dest = 'Kuala Lumpur International Airport, 64000 Sepang, Selangor'

# number 1
print('Number 1:')
# geocode places
um = navigation.geocode(origin)
print("Universiti Malaya: " + str(um))
umc = str(um[0]['geometry']['location']['lat']) + ',' + str(um[0]['geometry']['location']['lng'])
# print(umc)
lk = navigation.geocode('Kerinchi LRT Station')
print("LRT Kerinchi: " + str(lk))
lkc = str(lk[0]['geometry']['location']['lat']) + ',' + str(lk[0]['geometry']['location']['lng'])
# print(lkc)
ba = navigation.geocode('Taman Bukit Angkasa')
print("Taman Bukit Angkasa: " + str(ba))
bac = str(ba[0]['geometry']['location']['lat']) + ',' + str(ba[0]['geometry']['location']['lng'])
# print(bac)
fpk = navigation.geocode('Flat PKNS Kerinchi')
print("Flat PKNS Kerinchi: " + str(fpk))
fpkc = str(fpk[0]['geometry']['location']['lat']) + ',' + str(fpk[0]['geometry']['location']['lng'])
# print(fpkc)
lu = navigation.geocode('LRT Universiti')
print("LRT Universiti: " + str(lu))
luc = str(lu[0]['geometry']['location']['lat']) + ',' + str(lu[0]['geometry']['location']['lng'])
# print(luc)
pd = navigation.geocode('MRT Phileo Damansara')
print("MRT Phileo Damansara: " + str(pd))
pdc = str(pd[0]['geometry']['location']['lat']) + ',' + str(pd[0]['geometry']['location']['lng'])
# print(pdc)
ks = navigation.geocode('KL Sentral')
print("KL Sentral: " + str(ks))
ksc = str(ks[0]['geometry']['location']['lat']) + ',' + str(ks[0]['geometry']['location']['lng'])
# print(ksc)
ph = navigation.geocode('LRT Putra Heights')
print("LRT Putra Heights:" + str(ph))
phc = str(ph[0]['geometry']['location']['lat']) + ',' + str(ph[0]['geometry']['location']['lng'])
# print(phc)
mn = navigation.geocode('Muzium Negara')
print("Muzium Negara:" + str(mn))
mnc = str(mn[0]['geometry']['location']['lat']) + ',' + str(mn[0]['geometry']['location']['lng'])
# print(mnc)
bu = navigation.geocode('MRT Bandar Utama')
print("Bandar Utama: " + str(bu))
buc = str(bu[0]['geometry']['location']['lat']) + ',' + str(bu[0]['geometry']['location']['lng'])
# print(buc)
# ou = navigation.geocode('1 Utama Shopping Centre, Lot S327, Bandar Utama City Centre No1, Lebuh Bandar Utama, Bandar Utama, 47800 Petaling Jaya, Selangor')
# # print(ou)
# ouc = str(ou[0]['geometry']['location']['lat']) + ',' + str(ou[0]['geometry']['location']['lng'])
# # print(ouc)
lg = navigation.geocode('Gombak LRT Station')
print("LRT Gombak: " + str(lg))
lgc = str(lg[0]['geometry']['location']['lat']) + ',' + str(lg[0]['geometry']['location']['lng'])
klia = navigation.geocode(dest)
print("KLIA: " + str(klia))
kliac = str(klia[0]['geometry']['location']['lat']) + ',' + str(klia[0]['geometry']['location']['lng'])
# print(kliac)

print('Overall time travel by ome mode of transport:')
print('By road:')
road = navigation.directions(origin, dest, mode='driving')
print(road[0]['legs'][0]['distance']['text'])
print('By public transport (train+bus):')
publ = navigation.directions(origin, dest, mode='transit')
print(publ[0]['legs'][0]['distance']['text'])
print('By feet:')
walk = navigation.directions(origin, dest, mode='walking')
print(walk[0]['legs'][0]['distance']['text'])

# number 2
print('\nNumber 2:')
# set distance
# um to kerinchi by bus
umlk = navigation.distance_matrix(umc, lkc, mode='transit', transit_mode='bus')
dumlk = umlk['rows'][0]['elements'][0]['distance']['value']
print(str(umlk))
# um to lrt university by feet
umlu = navigation.distance_matrix(umc, luc, mode='walking')
dumlu = umlu['rows'][0]['elements'][0]['distance']['value']
print(str(umlu))
# um to mrt phileo damansara by bus
umpd = navigation.distance_matrix(umc, pdc, mode='transit', transit_mode='bus')
dumpd = umpd['rows'][0]['elements'][0]['distance']['value']
print(str(umpd))
# um to bukit angkasa by bus
umba = navigation.distance_matrix(umc, bac, mode='transit', transit_mode='bus')
dumba = umba['rows'][0]['elements'][0]['distance']['value']
print(str(umba))
# bukit angkasa tu flat pkns by bus
bafpk = navigation.distance_matrix(bac, fpkc, mode='transit', transit_mode='bus')
dbafpk = bafpk['rows'][0]['elements'][0]['distance']['value']
print(str(bafpk))
# flat pkns to lrt kerinchi by feet
fpklk = navigation.distance_matrix(fpkc, lkc, mode='walking')
dfpklk = fpklk['rows'][0]['elements'][0]['distance']['value']
print(str(fpklk))
# lrt kerinchi to lrt uni by train
lklu = navigation.distance_matrix(lkc, luc, mode='transit')
dlklu = lklu['rows'][0]['elements'][0]['distance']['value']
print(str(lklu))
# lrt kerinchi to kl sentral by train
lkks = navigation.distance_matrix(lkc, ksc, mode='transit')
dlkks = lkks['rows'][0]['elements'][0]['distance']['value']
print(str(lkks))
# lrt kerinchi to lrt gombak by train
lklg = navigation.distance_matrix(lkc, lgc, mode='transit')
dlklg = lklg['rows'][0]['elements'][0]['distance']['value']
print(str(lklg))
# lrt kerinchi to putra heights by train
lkph = navigation.distance_matrix(lkc, phc, mode='transit')
dlkph = lkph['rows'][0]['elements'][0]['distance']['value']
print(str(lkph))
# lrt uni to kl sentral by train
luks = navigation.distance_matrix(luc, ksc, mode='transit')
dluks = luks['rows'][0]['elements'][0]['distance']['value']
print(str(luks))
# lrt uni to mrt phileo by road (self-drive/grab)
lupd = navigation.distance_matrix(luc, pdc, mode='driving')
dlupd = lupd['rows'][0]['elements'][0]['distance']['value']
print(str(lupd))
# mrt phileo to muzium negara by train
pdmn = navigation.distance_matrix(pdc, mnc, mode='transit')
dpdmn = pdmn['rows'][0]['elements'][0]['distance']['value']
print(str(pdmn))
# muzium negara to bandar utama by bus
mnbu = navigation.distance_matrix(mnc, buc, mode='transit', transit_mode='bus')
dmnbu = mnbu['rows'][0]['elements'][0]['distance']['value']
print(str(mnbu))
# muzium negara to kl sentral by feet
mnks = navigation.distance_matrix(mnc, ksc, mode='walking')
dmnks = mnks['rows'][0]['elements'][0]['distance']['value']
print(str(mnks))
# lrt gombak to kl sentral
lgks = navigation.distance_matrix(lgc, ksc, mode='transit')
dlgks = lgks['rows'][0]['elements'][0]['distance']['value']
print(str(lgks))
# kl sentral to putra heights by road (self-drive/grab)
ksph = navigation.distance_matrix(ksc, phc, mode='driving')
dksph = ksph['rows'][0]['elements'][0]['distance']['value']
print(str(ksph))
# kl sentral to klia by road(self-drive/grab)
ksklia = navigation.distance_matrix(ksc, kliac, mode='driving')
dksklia = ksklia['rows'][0]['elements'][0]['distance']['value']
print(str(ksklia))
# pdbu = navigation.directions(pdc, buc, mode='transit')
# dpdbu = int(pdbu[0]['legs'][0]['distance']['value'])
# buou = navigation.distance_matrix(buc, ouc, mode='walking')
# dbuou = int(buou['rows'][0]['elements'][0]['distance']['value'])
# ouklia = navigation.distance_matrix(ouc, kliac, mode='transit', transit_mode='bus')
# print(ouklia)
# douklia = ouklia['rows'][0]['elements'][0]['distance']['value']
# print(douklia)
# buklia = navigation.directions(buc, kliac, mode='transit', transit_mode='bus')
# dbuklia = int(buklia[0]['legs'][0]['distance']['value'])
# mnklia = navigation.directions(mnc, klia, mode="driving")
# dmnklia = int(mnklia[0]['legs'][0]['distance']['value'])
# phklia = navigation.directions(phc, kliac, mode='transit')
# dphklia = int(phklia[0]['legs'][0]['distance']['value'])

Graph = {
    'University Malaya': {'LRT Kerinchi': dumlk, 'LRT Universiti': dlklu, 'MRT Phileo': dlupd, 'Bukit Angkasa': dumba},
    'LRT Kerinchi': {'KL Sentral': dlkks, 'LRT Putra Heights': dlkph, 'Gombak LRT Station': dlklg},
    'LRT Universiti': {'KL Sentral': dluks, 'LRT Putra Heights': dksph},
    'MRT Phileo': {'MRT Muzium Negara': dpdmn, 'MRT Bandar Utama': dmnbu},
    'KL Sentral': {'KLIA': dksklia},
    'LRT Putra Heights': {},
    'MRT Muzium Negara': {'KL Sentral': dmnks, 'MRT Bandar Utama': dmnbu},
    'MRT Bandar Utama': {},
    'Bukit Angkasa': {'Flat PKNS Kerinchi': dbafpk},
    'Flat PKNS Kerinchi': {'LRT Kerinchi': dfpklk},
    'Gombak LRT Station': {'KL Sentral': dlgks}
    # 'One Utama Bus Terminal': {'KLIA': douklia}
}

def Dijkstra(Graph, start, end=None):
    D = {}  # dictionary of final distances
    P = {}  # dictionary of predecessors
    Q = priorityDictionary ()  # estimated distances of non-final vertices
    Q[start] = 0

    for v in Q:
        D[v] = Q[v]
        if v == end:
            break
        for w in Graph[v]:
            vwLength = D[v] + Graph[v][w]
            if w in D:
                if vwLength < D[w]:
                    raise ValueError("Dijkstra: found better path to already-final vertex")
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v

    return (D, P)


def shortestPath(Graph, start, end):
    """
    Find a single shortest path from the given start vertex to the given
    end vertex. The input has the same conventions as Dijkstra(). The
    output is a list of the vertices in order along the shortest path.
    """

    D, P = Dijkstra (Graph, start, end)
    Path = []
    while 1:
        Path.append (end)
        if end == start:
            break
        end = P[end]
    Path.reverse ()
    return Path


def find_all_paths(allpath, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in allpath[start]:
        if node not in path:
            newpaths = find_all_paths (allpath, node, end, path)
        for newpath in newpaths:
            paths.append (newpath)
    return paths

print ('\nAll paths: ')
pprint.pprint(find_all_paths(Graph, 'University Malaya', 'KLIA'))
print ('\nThe shortest path is: ')
print (shortestPath (Graph, 'University Malaya', 'KLIA'))

# number 3
print('\nNumber 3:')

# straight line
lat_straight = [(um[0]['geometry']['location']['lat']), (klia[0]['geometry']['location']['lat'])]
long_straight = [(um[0]['geometry']['location']['lng']), (klia[0]['geometry']['location']['lng'])]
gmp.scatter(lat_straight, long_straight, color='red', size=200, marker=False)
gmp.plot(lat_straight, long_straight, color='#660d2b', edge_width=2.5)

# points
lat1 = [(um[0]['geometry']['location']['lat']), (lk[0]['geometry']['location']['lat']), (ks[0]['geometry']['location']['lat']), (klia[0]['geometry']['location']['lat'])]
long1 = [(um[0]['geometry']['location']['lng']), (lk[0]['geometry']['location']['lng']), (ks[0]['geometry']['location']['lng']), (klia[0]['geometry']['location']['lng'])]
gmp.scatter(lat1, long1, color='black', size=200, marker=False)
gmp.plot(lat1, long1, color='black', edge_width=2.5)

lat2 = [(um[0]['geometry']['location']['lat']), (lk[0]['geometry']['location']['lat']), (lg[0]['geometry']['location']['lat']), (ks[0]['geometry']['location']['lat']), (klia[0]['geometry']['location']['lat'])]
long2 = [(um[0]['geometry']['location']['lng']), (lk[0]['geometry']['location']['lng']), (lg[0]['geometry']['location']['lng']), (ks[0]['geometry']['location']['lng']), (klia[0]['geometry']['location']['lng'])]
gmp.scatter(lat2, long2, color='purple', size=200, marker=False)
gmp.plot(lat2, long2, color='purple', edge_width=2.5)

lat3 = [(um[0]['geometry']['location']['lat']), (lu[0]['geometry']['location']['lat']), (ks[0]['geometry']['location']['lat']), (klia[0]['geometry']['location']['lat'])]
long3 = [(um[0]['geometry']['location']['lng']), (lu[0]['geometry']['location']['lng']), (ks[0]['geometry']['location']['lng']), (klia[0]['geometry']['location']['lng'])]
gmp.scatter(lat3, long3, color='blue', size=200, marker=False)
gmp.plot(lat3, long3, color='blue', edge_width=2.5)

lat4 = [(um[0]['geometry']['location']['lat']), (pd[0]['geometry']['location']['lat']), (mn[0]['geometry']['location']['lat']), (ks[0]['geometry']['location']['lat']), (klia[0]['geometry']['location']['lat'])]
long4 = [(um[0]['geometry']['location']['lng']), (pd[0]['geometry']['location']['lng']), (mn[0]['geometry']['location']['lng']), (ks[0]['geometry']['location']['lng']), (klia[0]['geometry']['location']['lng'])]
gmp.scatter(lat4, long4, color='green', size=200, marker=False)
gmp.plot(lat4, long4, color='green', edge_width=2.5)

lat5 = [(um[0]['geometry']['location']['lat']), (ba[0]['geometry']['location']['lat']), (fpk[0]['geometry']['location']['lat']), (lk[0]['geometry']['location']['lat']), (ks[0]['geometry']['location']['lat']), (klia[0]['geometry']['location']['lat'])]
long5 = [(um[0]['geometry']['location']['lng']), (ba[0]['geometry']['location']['lng']), (fpk[0]['geometry']['location']['lng']), (lk[0]['geometry']['location']['lng']), (ks[0]['geometry']['location']['lng']), (klia[0]['geometry']['location']['lng'])]
gmp.scatter(lat5, long5, color='cyan', size=200, marker=False)
gmp.plot(lat5, long5, color='cyan', edge_width=2.5)

lat6 = [(um[0]['geometry']['location']['lat']), (ba[0]['geometry']['location']['lat']), (fpk[0]['geometry']['location']['lat']), (lk[0]['geometry']['location']['lat']), (lg[0]['geometry']['location']['lat']), (ks[0]['geometry']['location']['lat']), (klia[0]['geometry']['location']['lat'])]
long6 = [(um[0]['geometry']['location']['lng']), (ba[0]['geometry']['location']['lng']), (fpk[0]['geometry']['location']['lng']), (lk[0]['geometry']['location']['lng']), (lg[0]['geometry']['location']['lng']), (ks[0]['geometry']['location']['lng']), (klia[0]['geometry']['location']['lng'])]
gmp.scatter(lat6, long6, color='magenta', size=200, marker=False)
gmp.plot(lat6, long6, color='magenta', edge_width=2.5)

latbest = lat1
longbest = long1
gmp.scatter(latbest, longbest, color='red', size=200, marker=False)
gmp.plot(latbest, longbest, color='red', edge_width=2.5)

# output map
gmp.draw("map.html")
print('Map printed! Please check the file directory.')
