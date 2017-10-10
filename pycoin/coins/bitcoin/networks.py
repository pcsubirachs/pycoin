
from pycoin.serialize import h2b

from .ScriptTools import BitcoinScriptTools
from .Tx import Tx as BitcoinTx
from pycoin.block import Block as BitcoinBlock

from pycoin.networks.network import Network
from pycoin.ui.uiclass import UI
from pycoin.vm.PuzzleScripts import PuzzleScripts

_puzzle_script = PuzzleScripts(BitcoinScriptTools)


mainnet_ui = UI(_puzzle_script, address_prefix=h2b("00"), pay_to_script_prefix=h2b("05"), bech32_hrp='bc')


BitcoinMainnet = Network(
    'BTC', "Bitcoin", "mainnet",
    h2b("80"), h2b("00"), h2b("05"), h2b("0488ADE4"), h2b("0488B21E"),
    BitcoinTx, BitcoinBlock,
    h2b('F9BEB4D9'), 8333, [
        "seed.bitcoin.sipa.be", "dnsseed.bitcoin.dashjr.org",
        "bitseed.xf2.org", "dnsseed.bluematt.me",
    ],
    bech32_hrp='bc',
    ui=mainnet_ui
)


testnet_ui = UI(_puzzle_script, address_prefix=h2b("6f"), pay_to_script_prefix=h2b("c4"), bech32_hrp='tb')


BitcoinTestnet = Network(
    "XTN", "Bitcoin", "testnet3",
    h2b("ef"), h2b("6f"), h2b("c4"), h2b("04358394"), h2b("043587CF"),
    BitcoinTx, BitcoinBlock,
    h2b('0B110907'), 18333, [
        "bitcoin.petertodd.org", "testnet-seed.bitcoin.petertodd.org",
        "bluematt.me", "testnet-seed.bluematt.me"
    ],
    bech32_hrp='tb',
    ui=testnet_ui
)
