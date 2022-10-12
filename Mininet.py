from mininet.topo import Topo
class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        BerlinH=self.addHost('BerlinHost')
        HamburgH=self.addHost('HamburgHost')
        MonachiumH=self.addHost('MonachiumHost')
        KoloniaH=self.addHost('KoloniaHost')
        FrankfurtH=self.addHost('FrankfurtHost')
        StuttgardH=self.addHost('StuttgardHost')
        DusseldorfH=self.addHost('DusseldorfHost')
        LipskH=self.addHost('LipskHost')
        DortmundH=self.addHost('DortmundHost')
        EssenH=self.addHost('EssenHost')

        BerlinS = self.addHost('BerlinSwitch')
        HamburgS = self.addHost('HamburgSwitch')
        MonachiumS = self.addHost('MonachiumSwitch')
        KoloniaS = self.addHost('KoloniaSwitch')
        FrankfurtS = self.addHost('FrankfurtSwitch')
        StuttgardS = self.addHost('StuttgardSwitch')
        DusseldorfS = self.addHost('DusseldorfSwitch')
        LipskS = self.addHost('LipskSwitch')
        DortmundS = self.addHost('DortmundSwitch')
        EssenS = self.addHost('EssenSwitch')

        BerlinHS = self.addLink(BerlinH, BerlinS)
        HamburgHS = self.addLink(HamburgH, HamburgS)
        MonachiumHS = self.addLink(MonachiumH, MonachiumS)
        KoloniaHS = self.addLink(KoloniaH, KoloniaS)
        FrankfurtHS = self.addLink(FrankfurtH, FrankfurtS)
        StuttgardHS = self.addLink(StuttgardH, StuttgardS)
        DusseldorfHS = self.addLink(DusseldorfH, DusseldorfS)
        LipskHS = self.addLink(LipskH, LipskS)
        DortmundHS = self.addLink(DortmundH, DortmundS)
        EssenHS = self.addLink(EssenH, EssenS)

        Hamburg_Berlin = self.addLink(BerlinS, HamburgS)
        Hamburg_Kolonia = self.addLink(HamburgS, KoloniaS)
        Hamburg_Dortmund = self.addLink(HamburgS, DortmundS)
        Hamburg_Monachium = self.addLink(HamburgS, MonachiumS)
        Berlin_Kolonia = self.addLink(BerlinS, KoloniaS)
        Berlin_Lipsk = self.addLink(BerlinS, LipskS)
        Berlin_Monachium = self.addLink(BerlinS, MonachiumS)
        Lipsk_Frankfurt = self.addLink(LipskS, FrankfurtS)
        Monachium_Stuttgard = self.addLink(MonachiumS, StuttgardS)
        Monachium_Kolonia = self.addLink(MonachiumS, KoloniaS)
        Stuttgard_Frankfurt = self.addLink(StuttgardS, FrankfurtS)
        Kolonia_Dusseldorf = self.addLink(KoloniaS, DusseldorfS)
        Kolonia_Frankfurt = self.addLink(KoloniaS, FrankfurtS)
        Kolonia_Stuttgard = self.addLink(KoloniaS, StuttgardS)
        Essen_Dortmund = self.addLink(EssenS, DortmundS)
        Essen_Dusseldorf = self.addLink(EssenS, DusseldorfS)
        Dortmund_Dusseldorf = self.addLink(DortmundS, DusseldorfS)




