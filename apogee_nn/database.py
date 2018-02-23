from apogee_nn.models import Target, Neighbor
import pandas
from tqdm import trange


def sdss_explore_link(target_id):
    #Creates spectrum file name using the APOGEEcd fits id
    link = 'http://skyserver.sdss.org/dr14/en/tools/explore/summary.aspx?sid=' + target_id + '&apid='
     #link = "http://dr13.sdss3.org/irSpectrumDetail?locid=" + objid[2] + "&commiss=0&apogeeid=" + objid[1] + "&show_aspcap=True"
    return link


apogee_nn = pandas.read_csv('/Users/itamar/Documents/Work/apogee/OnlineData/apogee_nn.csv')
nof_objects = apogee_nn.shape[0]

Target.objects.all().delete()

#nof_objects = 101 #Testing

for i in trange(nof_objects):
    t = Target(target_id = apogee_nn.iloc[i]['APOGEE_ID'])
    for n_idx in range(apogee_nn.shape[1]):
        sdss_link = sdss_explore_link(t.target_id)
        t.neighbor_set.create(neighbor_id = apogee_nn.iloc[i][n_idx], neighbor_rank = n_idx, SDSS_link = sdss_link)
    t.save()

