from p2pool.bitcoin import networks

PARENT=networks.nets['digibyte']
SHARE_PERIOD=25
CHAIN_LENGTH=24*60*60//10
REAL_CHAIN_LENGTH=24*60*60//10
TARGET_LOOKBEHIND=200
SPREAD=150
IDENTIFIER='1c017dc97693f7d5'.decode('hex')
PREFIX='1c01bce905d5ead7'.decode('hex')
P2P_PORT=5031
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=True
WORKER_PORT=5030
BOOTSTRAP_ADDRS='crypto.office-on-the.net p2p-spb.xyz 46.188.44.20 siberia.mine.nu gigablock.mine.nu tomsk.mine.nu 45.32.210.32'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-dgb'
VERSION_CHECK = lambda v: None if 6160500 <= v else 'DigiByte version too old. Upgrade to 6.16.5 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['nversionbips', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
