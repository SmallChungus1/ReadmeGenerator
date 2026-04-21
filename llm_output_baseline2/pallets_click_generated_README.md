"
license = "BSD-3-Clause"
license-files = ["LICENSE.txt"]
maintainers = [{name = "Pallets", email = "contact@palletsprojects.com"}]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Typing :: Typed",
]
requires-python = ">=3.10"
dependencies = [
    "colorama; platform_system == 'Windows'",
]

[project.urls]
Donate = "https://palletsprojects.com/donate"
Documentation = "https://click.palletsprojects.com/"
Changes = "https://click.palletsprojects.com/page/changes/"
Source = "https://github.com/pallets/click/"
Chat = "https://discord.gg/pallets"

[dependency-groups]
dev = [
    "ruff",
    "tox",
    "tox-uv",
]
docs = [
    "myst-parser",
    "pallets-sphinx-themes",
    "sphinx",
    "sphinx-tabs",
    "sphinxcontrib-log-cabinet",
]
docs-auto = [
    "sphinx-autobuild",
]
gha-update = [
    "gha-update ; python_full_version >= '3.12'",
]
pre-commit = [
    "pre-commit",
    "pre-commit-uv",
]
tests = [
    "pytest",
]
typing = [
    "mypy",
    "pyright",
    "pytest",
]

[build-system]
requires = ["flit_core>=3.11,<4"]
build-backend = "flit_core.buildapi"

[tool.flit.module]
name = "click"

[tool.flit.sdist]
include = [
    "docs/",
    "tests/",
    "CHANGES.rst",
    "uv.lock"
]
exclude = [
    "docs/_build/",
]

[tool.uv]
default-groups = ["dev", "pre-commit", "tests", "typing"]

[tool.pytest.ini_options]
testpaths = ["tests"]
filterwarnings = [
    "error",
]
markers = [
    "stress: high-iteration stress tests for race conditions (deselect with '-m \"not stress\"')",
]
addopts = "-m 'not stress'"

[tool.coverage.run]
branch = true
source = ["click", "tests"]

[tool.coverage.paths]
source = ["src", "*/site-packages"]

[tool.coverage.report]
exclude_also = [
    "if t.TYPE_CHECKING",
    "raise NotImplementedError",
    ": \\.{3}",
]

[tool.mypy]
python_version = "3.10"
files = ["src", "tests/typing"]
show_error_codes = true
pretty = true
strict = true

[[tool.mypy.overrides]]
module = [
    "colorama.*",
]
ignore_missing_imports = true

[tool.pyright]
python_version = "3.10"
include = ["src", "tests/typing"]
typeCheckingMode = "basic"

[tool.ruff]
extend-exclude = ["examples/"]
src = ["src"]
fix = true
show-fixes = true
output-format = "full"

[tool.ruff.lint]
select = [
    "B",  # flake8-bugbear
    "E",  # pycodestyle error
    "F",  # pyflakes
    "I",  # isort
    "UP",  # pyupgrade
    "W",  # pycodestyle warning
]

[tool.ruff.lint.isort]
force-single-line = true
order-by-type = false

[tool.tox]
env_list = [
    "py3.14", "py3.13", "py3.12", "py3.11", "py3.10",
    "py3.14t",
    "pypy3.11",
    "stress-py3.14", "stress-py3.14t",
    "style",
    "typing",
    "docs",
]

[tool.tox.env_run_base]
description = "pytest on latest dependency versions"
runner = "uv-venv-lock-runner"
package = "wheel"
wheel_build_env = ".pkg"
constrain_package_deps = true
use_frozen_constraints = true
dependency_groups = ["tests"]
commands = [[
    "pytest", "-v", "--tb=short", "--basetemp={env_tmp_dir}",
    {replace = "posargs", default = [], extend = true},
]]

[tool.tox.env.stress]
description = "stress tests for stream lifecycle race conditions"
commands = [[
    "pytest", "-v", "--tb=short", "-x", "-m", "stress",
    "--basetemp={env_tmp_dir}",
    "--override-ini=addopts=",
    "tests/test_stream_lifecycle.py",
    {replace = "posargs", "default" = [], extend = true},
]]

[tool.tox.env.style]
description = "run all pre-commit hooks on all files"
dependency_groups = ["pre-commit"]
skip_install = true
commands = [["pre-commit", "run", "--all-files"]]

[tool.tox.env.typing]
description = "run static type checkers"
dependency_groups = ["typing"]
commands = [
    ["mypy"],
    ["pyright", "--ignoreexternal", "--verifytypes", "click"],
]

[tool.tox.env.docs]
description = "build docs"
dependency_groups = ["docs"]
commands = [["sphinx-build", "-E", "-W", "-b", "dirhtml", "docs", "docs/_build/dirhtml"]]

[tool.tox.env.docs-auto]
description = "continuously rebuild docs and start a local server"
dependency_groups = ["docs", "docs-auto"]
commands = [["sphinx-autobuild", "-W", "-b", "dirhtml", "--watch", "src", "docs", "docs/_build/dirhtml"]]

[tool.tox.env.update-actions]
description = "update GitHub Actions pins"
labels = ["update"]
dependency_groups = ["gha-update"]
skip_install = true
commands = [["gha-update"]]

[tool.tox.env.update-pre_commit]
description = "update pre-commit pins"
labels = ["update"]
dependency_groups = ["pre-commit"]
skip_install = true
commands = [["pre-commit", "autoupdate", "--freeze", "-j4"]]

[tool.tox.env.update-requirements]
description = "update uv lock"
labels = ["update"]
dependency_groups = []
no_default_groups = true
skip_install = true
commands = [["uv", "lock", {replace = "posargs", default = ["-U"], extend = true}]]


---
File: uv.lock
Size: 257774 bytes
Lines: 1621 [deps]
---
### Required Packages
alabaster==1.0.0, anyio==4.13.0, babel==2.18.0, cachetools==7.0.5, certifi==2026.2.25, cfgv==3.5.0, charset-normalizer==3.4.7, click==8.3.2, colorama==0.4.6, distlib==0.4.0
docutils==0.21.2, docutils==0.22.4, exceptiongroup==1.3.1, filelock==3.25.2, gha-update==0.2.0, h11==0.16.0, httpcore==1.0.9, httpx==0.28.1, identify==2.6.18, idna==3.11
imagesize==2.0.0, iniconfig==2.3.0, jinja2==3.1.6, librt==0.8.1, markdown-it-py==3.0.0, markdown-it-py==4.0.0, markupsafe==3.0.3, mdit-py-plugins==0.5.0, mdurl==0.1.2, mypy==1.20.0
mypy-extensions==1.1.0, myst-parser==4.0.1, myst-parser==5.0.0, nodeenv==1.10.0, packaging==26.0, pallets-sphinx-themes==2.5.0, pathspec==1.0.4, platformdirs==4.9.4, pluggy==1.6.0, pre-commit==4.5.1
pre-commit-uv==4.2.1, pygments==2.20.0, pyproject-api==1.10.0, pyright==1.1.408, pytest==9.0.2, python-discovery==1.2.1, pyyaml==6.0.3, requests==2.33.1, roman-numerals==4.1.0, ruff==0.15.9
snowballstemmer==3.0.1, sphinx==8.1.3, sphinx==9.0.4, sphinx==9.1.0, sphinx-autobuild==2024.10.3, sphinx-autobuild==2025.8.25, sphinx-notfound-page==1.1.0, sphinx-tabs==3.5.0, sphinxcontrib-applehelp==2.0.0, sphinxcontrib-devhelp==2.0.0
sphinxcontrib-htmlhelp==2.1.0, sphinxcontrib-jsmath==1.0.1, sphinxcontrib-log-cabinet==1.0.1, sphinxcontrib-qthelp==2.0.0, sphinxcontrib-serializinghtml==2.0.0, starlette==1.0.0, tomli==2.4.1, tomli-w==1.2.0, tox==4.52.0, tox-uv==1.34.0
tox-uv-bare==1.34.0, typing-extensions==4.15.0, urllib3==2.6.3, uv==0.11.3, uvicorn==0.43.0, virtualenv==21.2.0, watchfiles==1.1.1, websockets==16.0

---
File: src/click/__init__.py
Size: 4596 bytes
Lines: 123
---
from .core import Argument as Argument
from .core import Command as Command
from .core import CommandCollection as CommandCollection
from .core import Context as Context
from .core import Group as Group
from .core import Option as Option
from .core import Parameter as Parameter
from .decorators import argument as argument
from .decorators import command as command
from .decorators import confirmation_option as confirmation_option
from .decorators import group as group
from .decorators import help_option as help_option
from .decorators import make_pass_decorator as make_pass_decorator
from .decorators import option as option
from .decorators import pass_context as pass_context
from .decorators import pass_obj as pass_obj
from .decorators import password_option as password_option
from .decorators import version_option as version_option
from .exceptions import Abort as Abort
from .exceptions import BadArgumentUsage as BadArgumentUsage
from .exceptions import BadOptionUsage as BadOptionUsage
from .exceptions import BadParameter as BadParameter
from .exceptions import ClickException as ClickException
from .exceptions import FileError as FileError
from .exceptions import MissingParameter as MissingParameter
from .exceptions import NoSuchOption as NoSuchOption
from .exceptions import UsageError as UsageError
from .formatting import HelpFormatter as HelpFormatter
from .formatting import wrap_text as wrap_text
from .globals import get_current_context as get_current_context
from .termui import clear as clear
from .termui import confirm as confirm
from .termui import echo_via_pager as echo_via_pager
from .termui import edit as edit
from .termui import getchar as getchar
from .termui import launch as launch
from .termui import pause as pause
from .termui import progressbar as progressbar
from .termui import prompt as prompt
from .termui import secho as secho
from .termui import style as style
from .termui import unstyle as unstyle
from .types import BOOL as BOOL
from .types import Choice as Choice
from .types import DateTime as DateTime
from .types import File as File
from .types import FLOAT as FLOAT
from .types import FloatRange as FloatRange
from .types import INT as INT
from .types import IntRange as IntRange
from .types import ParamType as ParamType
from .types import Path as Path
from .types import STRING as STRING
from .types import Tuple as Tuple
from .types import UNPROCESSED as UNPROCESSED
from .types import UUID as UUID
from .utils import echo as echo
from .utils import format_filename as format_filename
from .utils import get_app_dir as get_app_dir
from .utils import get_binary_stream as get_binary_stream
from .utils import get_text_stream as get_text_stream
from .utils import open_file as open_file

def __getattr__(name: str) -> object:
    import warnings
    from .core import _BaseCommand
    from .core import _MultiCommand
    from .parser import _OptionParser
    import importlib.metadata
    import warnings
    warnings.warn(
        f"click.{name} is not a public API and may be removed in a future version.",
        FutureWarning,
    )
    return getattr(importlib.metadata, name)
---
File: src/click/_compat.py
Size: 19315 bytes
Lines: 622
---
import codecs
import collections.abc as cabc
import io
import os
import re
import sys
import typing as t
from types import TracebackType
from weakref import WeakKeyDictionary
def _make_text_stream(
def is_ascii_encoding(encoding: str) -> bool:
def get_best_encoding(stream: t.IO[t.Any]) -> str:
class _NonClosingTextIOWrapper(io.TextIOWrapper):
    def __init__(
    def __del__(self) -> None:
    def isatty(self) -> bool:
class _FixupStream:
    def __init__(
    def __getattr__(self, name: str) -> t.Any:
    def read1(self, size: int) -> bytes:
    def readable(self) -> bool:
    def writable(self) -> bool:
    def seekable(self) -> bool:
def _is_binary_reader(stream: t.IO[t.Any], default: bool = False) -> bool:
def _is_binary_writer(stream: t.IO[t.Any], default: bool = False) -> bool:
def _find_binary_reader(stream: t.IO[t.Any]) -> t.BinaryIO | None:
def _find_binary_writer(stream: t.IO[t.Any]) -> t.BinaryIO | None:
def _stream_is_misconfigured(stream: t.TextIO) -> bool:
def _is_compat_stream_attr(stream: t.TextIO, attr: str, value: str | None) -> bool:
def _is_compatible_text_stream(
def _force_correct_text_stream(
def _force_correct_text_reader(
def _force_correct_text_writer(
def get_binary_stdin() -> t.BinaryIO:
def get_binary_stdout() -> t.BinaryIO:
def get_binary_stderr() -> t.BinaryIO:
def get_text_stdin(encoding: str | None = None, errors: str | None = None) -> t.TextIO:
def get_text_stdout(encoding: str | None = None, errors: str | None = None). -> t.TextIO:
def get_text_stderr(encoding: str | None = None, errors: str | None = None) -> t.TextIO:
def _wrap_io_open(
def open_stream(
    import errno
    import random
class _AtomicFile:
    def __init__(self, f: t.IO[t.Any], tmp_filename: str, real_filename: str) -> None:
    def name(self) -> str:
    def close(self, delete: bool = False) -> None:
    def __getattr__(self, name: str) -> t.Any:
    def __enter__(self) -> _AtomicFile:
    def __exit__(
    def __repr__(self) -> str:
def strip_ansi(value: str) -> str:
def _is_jupyter_kernel_output(stream: t.IO[t.Any]) -> bool:
def should_strip_ansi(
    from ._winconsole import _get_windows_console_stream
    def _get_argv_encoding() -> str:
        import locale
    def auto_wrap_for_ansi(stream: t.TextIO, color: bool | None = None) -> t.TextIO:
        import colorama
        def _safe_write(s: str) -> int:
    def _get_argv_encoding() -> str:
    def _get_windows_console_stream(
def term_len(x: str) -> int:
def isatty(stream: t.IO[t.Any]) -> bool:
def _make_cached_stream_func(
    def func() -> t.TextIO | None:

---
File: src/click/_termui_impl.py
Size: 27945 bytes
Lines: 852
---
import collections.abc as cabc
import contextlib
import math
import os
import shlex
import sys
import time
import typing as t
from gettext import gettext as _
from io import StringIO
from pathlib import Path
from types import TracebackType
from ._compat import _default_text_stdout
from ._compat import CYGWIN
from ._compat import get_best_encoding
from ._compat import isatty
from ._compat import open_stream
from ._compat import strip_ansi
from ._compat import term_len
from ._compat import WIN
from .exceptions import ClickException
from .utils import echo
class ProgressBar(t.Generic[V]):
    def __init__(
            from operator import length_hint
    def __enter__(self) -> ProgressBar[V]:
    def __exit__(
    def __iter__(self) -> cabc.Iterator[V]:
    def __next__(self) -> V:
    def render_finish(self) -> None:
    def pct(self) -> float:
    def time_per_iteration(self) -> float:
    def eta(self) -> float:
    def format_eta(self) -> str:
    def format_pos(self) -> str:
    def format_pct(self). -> str:
    def format_bar(self) -> str:
    def format_progress_line(self) -> str:
    def render_progress(self) -> None:
            import shutil
    def make_step(self, n_steps: int) -> None:
    def update(self, n_steps: int, current_item: V | None = None) -> None:
    def finish(self) -> None:
    def generator(self) -> cabc.Iterator[V]:
def pager(generator: cabc.Iterable[str], color: bool | None = None) -> None:
    import tempfile
def _pipepager(
    import shutil
    import subprocess
def _tempfilepager(
    import shutil
    import subprocess
    import tempfile
def _nullpager(
class Editor:
    def __init__(
    def get_editor(self) -> str:
        from shutil import which
    def edit_files(self, filenames: cabc.Iterable[str]) -> None:
        import subprocess
    def edit(self, text: bytes | bytearray) -> bytes | None: ...
    def edit(self, text: str | None) -> str | None: ...
    def edit(self, text: str | bytes | bytearray | None) -> str | bytes | None:
        import tempfile
def open_url(url: str