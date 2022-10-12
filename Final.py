from mininet.topo import Topo
class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        BerlinH=self.addHost('BH')
        HamburgH=self.addHost('HH')
        MonachiumH=self.addHost('MH')
        KoloniaH=self.addHost('KH')
        FrankfurtH=self.addHost('FH')
        StuttgardH=self.addHost('SH')
        DusseldorfH=self.addHost('DH')
        LipskH=self.addHost('LH')
        DortmundH=self.addHost('DortH')
        EssenH=self.addHost('EH')

        BerlinS = self.addSwitch('s1')
        HamburgS = self.addSwitch('s2')
        MonachiumS = self.addSwitch('s3')
        KoloniaS = self.addSwitch('s4')
        FrankfurtS = self.addSwitch('s5')
        StuttgardS = self.addSwitch('s6')
        DusseldorfS = self.addSwitch('s7')
        LipskS = self.addSwitch('s8')
        DortmundS = self.addSwitch('s9')
        EssenS = self.addSwitch('s10')

        self.addLink(BerlinH, BerlinS)
        self.addLink(HamburgH, HamburgS)
        self.addLink(MonachiumH, MonachiumS)
        self.addLink(KoloniaH, KoloniaS)
        self.addLink(FrankfurtH, FrankfurtS)
        self.addLink(StuttgardH, StuttgardS)
        self.addLink(DusseldorfH, DusseldorfS)
        self.addLink(LipskH, LipskS)
        self.addLink(DortmundH, DortmundS)
        self.addLink(EssenH, EssenS)

        self.addLink(BerlinS, HamburgS)
        self.addLink(HamburgS, DortmundS)
        self.addLink(DortmundS, EssenS)
        self.addLink(BerlinS, KoloniaS)
        self.addLink(KoloniaS, DusseldorfS)
        self.addLink(KoloniaS, StuttgardS)
        self.addLink(BerlinS, MonachiumS)
        self.addLink(MonachiumS, FrankfurtS)
        self.addLink(FrankfurtS, LipskS)

topos = {'MyTopo': (lambda: MyTopo())}

