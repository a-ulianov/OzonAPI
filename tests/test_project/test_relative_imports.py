import pathlib
import pytest


class TestRelativeImports:
    """Тест на отсутствие абсолютных путей в импортах проекта."""

    def test_relative_imports(self):
        """Проверяет отсутствие в проекте импортов с 'src'."""

        src_dir = pathlib.Path("src")

        files_with_src_imports = []

        for py_file in src_dir.rglob("*.py"):
            content = py_file.read_text(encoding="utf-8")

            for line_num, line in enumerate(content.splitlines(), 1):
                if line.strip().startswith('from src.') or line.strip().startswith('import src.'):
                    relative_path = py_file.relative_to(src_dir)
                    files_with_src_imports.append(f"{relative_path}:{line_num}")

        if files_with_src_imports:
            error_msg = (
                "Найдены файлы с некорректными импортами:\n" +
                "\n".join(f"  - {file}" for file in files_with_src_imports)
            )
            pytest.fail(error_msg)