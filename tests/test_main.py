import runpy

import pytest


def test_main_invokes_cli(monkeypatch):
    called = {"value": False}

    def fake_cli():
        called["value"] = True
        raise SystemExit(0)

    monkeypatch.setattr("mvn_tree_visualizer.cli.cli", fake_cli)

    with pytest.raises(SystemExit):
        runpy.run_module("mvn_tree_visualizer.__main__", run_name="__main__")

    assert called["value"] is True
