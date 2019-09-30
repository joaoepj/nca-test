from mininet.net import Mininet
from mininet.topo import LinearTopo
from mininet.cli import CLI

MyTopo = LinearTopo(k=2)
net = Mininet(topo=MyTopo)


net.start()

h1, h2  = net.hosts[0], net.hosts[1]
print CLI(net, 'dpctl dump-flows')
print h1.cmd('ping -c10 %s' % h2.IP())


net.stop()
