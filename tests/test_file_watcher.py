import types

from mvn_tree_visualizer.file_watcher import DependencyFileHandler, FileWatcher


def test_dependency_file_handler_calls_callback_on_match():
    called = []

    def callback():
        called.append(True)

    handler = DependencyFileHandler("maven_dependency_file", callback)

    event_wrong = types.SimpleNamespace(is_directory=False, src_path="/tmp/other")
    event_dir = types.SimpleNamespace(is_directory=True, src_path="/tmp/maven_dependency_file")
    event_match = types.SimpleNamespace(is_directory=False, src_path="/tmp/maven_dependency_file")

    handler.on_modified(event_wrong)
    handler.on_modified(event_dir)
    handler.on_modified(event_match)

    assert called == [True]


def test_file_watcher_start_and_stop(monkeypatch):
    events = {"scheduled": False, "started": False, "stopped": False, "joined": False}

    class DummyObserver:
        def schedule(self, *_args, **_kwargs):
            events["scheduled"] = True

        def start(self):
            events["started"] = True

        def stop(self):
            events["stopped"] = True

        def join(self):
            events["joined"] = True

    monkeypatch.setattr("mvn_tree_visualizer.file_watcher.Observer", DummyObserver)

    watcher = FileWatcher("/tmp", "maven_dependency_file", lambda: None)
    watcher.start()
    watcher.stop()

    assert events["scheduled"] is True
    assert events["started"] is True
    assert events["stopped"] is True
    assert events["joined"] is True


def test_file_watcher_wait_calls_stop_on_keyboard_interrupt(monkeypatch):
    events = {"stopped": False}

    class DummyObserver:
        def schedule(self, *_args, **_kwargs):
            pass

        def start(self):
            pass

        def stop(self):
            pass

        def join(self):
            pass

    monkeypatch.setattr("mvn_tree_visualizer.file_watcher.Observer", DummyObserver)

    watcher = FileWatcher("/tmp", "maven_dependency_file", lambda: None)

    def stop_wrapper():
        events["stopped"] = True

    monkeypatch.setattr(watcher, "stop", stop_wrapper)
    monkeypatch.setattr("mvn_tree_visualizer.file_watcher.time.sleep", lambda _s: (_ for _ in ()).throw(KeyboardInterrupt))

    watcher.wait()

    assert events["stopped"] is True
