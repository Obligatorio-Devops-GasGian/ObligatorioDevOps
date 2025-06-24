import subprocess

def test_app_runs():
    import subprocess
    try:
        result = subprocess.run(
            ["python", "-m", "vote.app"],
            check=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        print("Salida:", result.stdout)
        assert "error" not in result.stdout.lower()
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el comando:", e.stderr)
        raise
