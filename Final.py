import mininet.link
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

        self.addLink(BerlinS, HamburgS, cls=mininet.link.TCLink, bw=10, delay='1.405ms')
        self.addLink(HamburgS, DortmundS, cls=mininet.link.TCLink, bw=10, delay='1.6ms')
        self.addLink(DortmundS, EssenS, cls=mininet.link.TCLink, bw=10, delay='0.174ms')
        self.addLink(BerlinS, KoloniaS, cls=mininet.link.TCLink, bw=10, delay='2.69ms')
        self.addLink(KoloniaS, DusseldorfS, cls=mininet.link.TCLink, bw=10, delay='0.1895ms')
        self.addLink(KoloniaS, StuttgardS, cls=mininet.link.TCLink, bw=10, delay='1.65ms')
        self.addLink(BerlinS, MonachiumS, cls=mininet.link.TCLink, bw=10, delay='2.84ms')
        self.addLink(MonachiumS, FrankfurtS, cls=mininet.link.TCLink, bw=10, delay='1.73ms')
        self.addLink(FrankfurtS, LipskS, cls=mininet.link.TCLink, bw=10, delay='1.66ms')


topos = {'MyTopo': (lambda: MyTopo())}

