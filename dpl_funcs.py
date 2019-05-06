
def read_by_name(fname):
    fpath = dataDir + fname
    dt = sio.loadmat(fpath)['y']
    dt = dt.transpose()
    return np.delete(dt, 29, axis=1)
    

def read_by_spk_tr(subject, spk, trial_number):
    # generate the name
    fn = 'FARAH_'+'sub0%0.2d'%subject+'_LS'+str(spk)+'_'+str(trial_number)
    return fn 

def gen_nameLists(subjectNumber, speakerSide):
    ssides = [1,4]
    if speakerSide not in ssides:
        print("speaker side is 1 or 4")
        #break
    
    namelists = []
    for trial in range(1,5):
        fname = 'FARAH_'+'sub0%0.2d'%subjectNumber+'_LS'+str(speakerSide)+'_'+str(trial)
        namelists.append(fname)
    return namelists


