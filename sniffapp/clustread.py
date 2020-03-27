import re
import os
from .models import GWCandidate, GWevent, GWfield

class ClustRead2:
    def __init__(self, filename):
        fin = open(filename, 'r')
        for line in fin:
            if 'RAaverage' in line:
                entries = line.split()
                namerow = []
                for e in entries:
                    e = e.replace('#', '')
                    namerow.append(e)
                if line.startswith('#ID'):
                    break
                if line.startswith('# ID'):
                    namerow.remove('')
        for i in range(len(namerow)):
            data = []
            openfile = open(filename, 'r')
            for line in openfile:
                if ('cmp' not in line) and ('#ID' not in line) and ('# ID' not in line):
                    dataentries = line.split()
                    data.append(dataentries[i])
                    if line.startswith('#ID'):
                        break
            self.__dict__[namerow[i]] = data
        fieldname = re.findall('^[^_]+', filename)
        self.__dict__['field'] = fieldname[0]
        gwevent = filename.split('_1.')[1]
        self.__dict__['gwevent'] = gwevent
        imagedir = filename.split('.diff')[0]
        self.__dict__['imagedir'] = imagedir


class ClustRead3:
    def __init__(self, filename):
        fin = open(filename, 'r')
        namerow3 = []
        for line in fin:
            if 'peakflux' in line:
                nameentries = line.split()
                for e in nameentries:
                    a = e.replace('#', '')
                    namerow3.append(a)
                if line.startswith('#ID'):
                    break
        for i in range(len(namerow3)):
            data3 = []
            openfile = open(filename, 'r')
            for line in openfile:
                if ('0x00000000' not in line) and ('#ID' not in line)\
                        and ('MJD' not in line) and ('data' not in line):
                    dataentries = line.split()
                    data3.append(dataentries[i])
            self.__dict__[namerow3[i]] = data3
        fieldname = re.findall('^[^_]+', filename)
        self.__dict__['field'] = fieldname
        gwevent = filename.split('_1.')[1]
        self.__dict__['gwevent'] = gwevent
        imagedir = filename.split('.diff')[0]
        self.__dict__['imagedir'] = imagedir


def clustload(path_to_folder):
    files = []
    sampleclustfile = ClustRead2('s036578_1.gw190814_1.6.diff.clusters')
    gweventforfile = GWevent(gwevent=sampleclustfile.gwevent)
    gweventforfile.save()
    for i in os.listdir(path_to_folder):
        if i.endswith('.clusters'):
            files.append(i)
    for file in files:
        clustfile = ClustRead2(file)
        fieldforfile = GWfield(field=clustfile.field, gwevent=gweventforfile)
        fieldforfile.save()
        for i in range(len(clustfile.RAaverage)):
            cand = GWCandidate(ra=clustfile.RAaverage[i], dec=clustfile.DECaverage[i], candidate_id=clustfile.ID[i],
                               imagedir=clustfile.imagedir, field=fieldforfile, gwevent=gweventforfile)
            cand.save()





#os.chdir('/Users/ChuyNunez/documents/research/websniff/websniff/sniffapp/clusters')
#files = []
#for i in os.listdir('/Users/ChuyNunez/documents/research/websniff/websniff/sniffapp/clusters'):
    #if i.endswith('.clusters'):
        #files.append(i)
#for file in files:
    #clustfile = ClustRead2(file)
    #print(file)
#clustload('/Users/ChuyNunez/documents/research/websniff/websniff/sniffapp/clusters')
#clustfile = ClustRead2('s041492_1.gw190814_1.3.diff.clusters')
#print(clustfile.RAaverage)
#print(clustfile.RAaverage)
#print(os.getcwd())



