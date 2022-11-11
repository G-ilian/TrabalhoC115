from mininet.topo import Topo
#-*- coding: utf-8 -*-
class MyTopo( Topo ):
    "10 host 5 switch custom topology"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add switches
        mainSwitch=self.addSwitch('s1') # Switch raiz para a aplicação
        switch2=self.addSwitch('s2')
        switch3=self.addSwitch('s3')
        switch4=self.addSwitch('s4')
        switch5=self.addSwitch('s5')

        # Add hosts
        host1=self.addHost('h1')
        host2=self.addHost('h2')
        host3=self.addHost('h3')
        host4=self.addHost('h4')
        host5=self.addHost('h5')
        host6=self.addHost('h6')
        host7=self.addHost('h7')
        host8=self.addHost('h8')
        host9=self.addHost('h9')
        host10=self.addHost('h10')


        # Add links
        # Connection switchs with switchs
        self.addLink(mainSwitch,switch2)
        self.addLink(mainSwitch,switch3)
        self.addLink(mainSwitch,switch4)
        self.addLink(mainSwitch,switch5)
        # Connection Switchs with hosts
        # Switch 2
        self.addLink(switch2,host1)
        self.addLink(switch2,host8)
        self.addLink(switch2,host9)
        # Switch 3
        self.addLink(switch3,host10)
        self.addLink(switch3,host2)
        self.addLink(switch3,host3)
        # Switch 4
        self.addLink(switch4,host7)
        # Switch 5
        self.addLink(switch5,host6)
        self.addLink(switch5,host5)
        self.addLink(switch5,host4)

        

topos = { 'mytopo': ( lambda: MyTopo() ) }
