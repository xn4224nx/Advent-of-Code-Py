"""
Tests for the main script.
"""

from main import ParticleSwarm


def test_parse_data_exp01():
    test = ParticleSwarm("./data/example_01.txt")
    assert test.pnt == (0, 0, 0)
    assert test.particles == [
        [(3, 0, 0), (2, 0, 0), (-1, 0, 0)],
        [(4, 0, 0), (0, 0, 0), (-2, 0, 0)],
    ]


def test_parse_data_exp02():
    test = ParticleSwarm("./data/example_02.txt")
    assert test.pnt == (0, 0, 0)
    assert test.particles == [
        [(4, 0, 0), (1, 0, 0), (-1, 0, 0)],
        [(2, 0, 0), (-2, 0, 0), (-2, 0, 0)],
    ]


def test_parse_data_exp03():
    test = ParticleSwarm("./data/example_03.txt")
    assert test.pnt == (0, 0, 0)
    assert test.particles == [
        [(4, 0, 0), (0, 0, 0), (-1, 0, 0)],
        [(-2, 0, 0), (-4, 0, 0), (-2, 0, 0)],
    ]


def test_parse_data_exp04():
    test = ParticleSwarm("./data/example_04.txt")
    assert test.pnt == (0, 0, 0)
    assert test.particles == [
        [(3, 0, 0), (-1, 0, 0), (-1, 0, 0)],
        [(-8, 0, 0), (-6, 0, 0), (-2, 0, 0)],
    ]


def test_step_exp01():
    test = ParticleSwarm("./data/example_01.txt")
    test.particles = [
        [(3, 0, 0), (2, 0, 0), (-1, 0, 0)],
        [(4, 0, 0), (0, 0, 0), (-2, 0, 0)],
    ]
    test.tick()
    assert test.particles == [
        [(4, 0, 0), (1, 0, 0), (-1, 0, 0)],
        [(2, 0, 0), (-2, 0, 0), (-2, 0, 0)],
    ]


def test_step_exp02():
    test = ParticleSwarm("./data/example_01.txt")
    test.particles = [
        [(4, 0, 0), (1, 0, 0), (-1, 0, 0)],
        [(2, 0, 0), (-2, 0, 0), (-2, 0, 0)],
    ]
    test.tick()
    assert test.particles == [
        [(4, 0, 0), (0, 0, 0), (-1, 0, 0)],
        [(-2, 0, 0), (-4, 0, 0), (-2, 0, 0)],
    ]


def test_step_exp03():
    test = ParticleSwarm("./data/example_01.txt")
    test.particles = [
        [(4, 0, 0), (0, 0, 0), (-1, 0, 0)],
        [(-2, 0, 0), (-4, 0, 0), (-2, 0, 0)],
    ]
    test.tick()
    assert test.particles == [
        [(3, 0, 0), (-1, 0, 0), (-1, 0, 0)],
        [(-8, 0, 0), (-6, 0, 0), (-2, 0, 0)],
    ]


def test_step_exp04():
    test = ParticleSwarm("./data/example_01.txt")
    test.particles = [
        [(3, 0, 0), (2, 0, 0), (-1, 0, 0)],
        [(4, 0, 0), (0, 0, 0), (-2, 0, 0)],
    ]
    test.tick()
    test.tick()
    test.tick()
    assert test.particles == [
        [(3, 0, 0), (-1, 0, 0), (-1, 0, 0)],
        [(-8, 0, 0), (-6, 0, 0), (-2, 0, 0)],
    ]


def test_particle_dists_exp01():
    test = ParticleSwarm("./data/example_01.txt")
    test.particles = [
        [(3, 0, 0), (2, 0, 0), (-1, 0, 0)],
        [(4, 0, 0), (0, 0, 0), (-2, 0, 0)],
    ]
    assert test.particle_dists() == [3, 4]


def test_particle_dists_exp02():
    test = ParticleSwarm("./data/example_01.txt")
    test.particles = [
        [(4, 0, 0), (1, 0, 0), (-1, 0, 0)],
        [(2, 0, 0), (-2, 0, 0), (-2, 0, 0)],
    ]
    assert test.particle_dists() == [4, 2]


def test_particle_dists_exp03():
    test = ParticleSwarm("./data/example_01.txt")
    test.particles = [
        [(4, 0, 0), (0, 0, 0), (-1, 0, 0)],
        [(-2, 0, 0), (-4, 0, 0), (-2, 0, 0)],
    ]
    assert test.particle_dists() == [4, 2]


def test_particle_dists_exp04():
    test = ParticleSwarm("./data/example_01.txt")
    test.particles = [
        [(3, 0, 0), (-1, 0, 0), (-1, 0, 0)],
        [(-8, 0, 0), (-6, 0, 0), (-2, 0, 0)],
    ]
    assert test.particle_dists() == [3, 8]


def test_long_term_closest_exp01():
    assert ParticleSwarm("./data/example_01.txt").long_term_closest()[0] == 0


def test_long_term_closest_exp02():
    assert ParticleSwarm("./data/example_05.txt").long_term_closest()[1] == 1
