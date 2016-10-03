import argparse
import coverage
import subprocess


parser = argparse.ArgumentParser(description="Parse coverage arguments")
parser.add_argument('--html', action='store_true', help="Generate reports as html")
parser.add_argument('-d', action='store_true', help="Destination directory for generate html")

args = parser.parse_args()

if __name__ == "__main__":
    cov = coverage.Coverage(omit=['venv/*', 'app/tests/*', './runtests.py'], source='.', branch=True)
    cov.start()
    import app.tests as tests

    tests.runner.run(tests.suite)

    cov.stop()
    cov.save()
    if args.html:
        cov.html_report(directory="app/tests/coverage")
        print("Reports generated:", "app/tests/coverage/index.html")
        subprocess.Popen(["open", 'app/tests/coverage/index.html'])
    else:
        cov.report()
