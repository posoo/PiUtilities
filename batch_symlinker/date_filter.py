import os
import click
from datetime import datetime


class DirPath:
    def __init__(self, dir_path):
        super().__init__()
        if not os.path.isdir(dir_path):
            raise RuntimeError(
                "The path specified is not a directory :{}".format(dir_path)
            )
        self.dir_path = dir_path
        # self.paths inside the specified directory
        self.paths = os.listdir(self.dir_path)

    def date_filter(self, start, end):
        """
        start/end: specify the date with format 'year-month-date'
        """
        if start is None and end is None:
            raise (
                SyntaxError(
                    "You should specify at least one date between 'start' and 'end'."
                )
            )
        elif start is None and end is not None:
            end_dt = datetime.strptime(end, "%Y-%m-%d")
            end_dt = end_dt.replace(day=end_dt.day + 1)
            ans = list(
                filter(
                    lambda f: os.path.getctime(os.path.join(self.dir_path, f))
                    <= end_dt.timestamp(),
                    self.paths,
                )
            )
            print(
                "Found {} files in {}\nBefore {}".format(
                    len(ans),
                    self.dir_path,
                    datetime.fromtimestamp(end_dt.timestamp() - 0.000001),
                )
            )
        elif start is not None and end is None:
            start_dt = datetime.strptime(start, "%Y-%m-%d")
            ans = list(
                filter(
                    lambda f: start_dt.timestamp()
                    <= os.path.getctime(os.path.join(self.dir_path, f)),
                    self.paths,
                )
            )
            print(
                "Found {} files in {}\nAfter {}".format(
                    len(ans), self.dir_path, start_dt
                )
            )
        else:
            start_dt = datetime.strptime(start, "%Y-%m-%d")
            end_dt = datetime.strptime(end, "%Y-%m-%d")
            end_dt = end_dt.replace(day=end_dt.day + 1)
            ans = list(
                filter(
                    lambda f: start_dt.timestamp()
                    <= os.path.getctime(os.path.join(self.dir_path, f))
                    < end_dt.timestamp(),
                    self.paths,
                )
            )
            print(
                "Found {} files in {}\nFrom {} to {}".format(
                    len(ans),
                    self.dir_path,
                    start_dt,
                    datetime.fromtimestamp(end_dt.timestamp() - 0.000001),
                )
            )
        return ans


@click.command()
@click.option(
    "--dir_path", required=True, type=str, help="Specify the dir you want to scan."
)
@click.option(
    "--start", type=str, help='Specify the start date in the form of "%Y-%m-%d".'
)
@click.option(
    "--end", type=str, help='Specify the start end in the form of "%Y-%m-%d".'
)
@click.option(
    "--save_path", type=str, help='Specify the path to save filtered file names.'
)
def cmd(dir_path, start, end, save_path):
    dir = DirPath(dir_path)
    ans = dir.date_filter(start, end)
    if save_path is not None:
        with open(save_path, 'w') as out:
            for f in ans:
                out.write('{}\n'.format(f))
    # print(ans)


if __name__ == "__main__":
    cmd()
