import os
import subprocess

import pytest

from flanker.flanker import *


cwd = os.getcwd()
data_dir = 'tests/data'  # Test from project root

def run(cmd, cwd=cwd):  # Helper for CLI testing
    return subprocess.run(cmd,
                        cwd=cwd,
                        shell=True,
                        check=True,
                        universal_newlines=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)

def test_default():
    run('flanker -i test.fasta -g blaKPC-2 -w 100', cwd=data_dir)
    run('rm *flank.fasta *_resfinder', cwd=data_dir)

def test_mm():
    run('flanker -i test.fasta -g blaKPC-2 blaKPC-3  -m mm -w 100', cwd=data_dir)
    run('rm *flank.fasta *_resfinder', cwd=data_dir)

def test_circ_inc():
    run('flanker -i test.fasta -g blaKPC-2 -w 100 -circ -inc', cwd=data_dir)
    run('rm *flank.fasta *_resfinder', cwd=data_dir)

def test_cluster():
    run('flanker -i test.fasta -g blaKPC-2 -w 100 -cl', cwd=data_dir)
    run('rm *flank.fasta *_resfinder out*', cwd=data_dir)

def test_salami():
    run('flanker -i test.fasta -g blaKPC-2 -w 100 -m sm', cwd=data_dir)
    run('rm *flank.fasta *_resfinder', cwd=data_dir)
