import click
import os


@click.command()
@click.option("--files", type=str, required=True, help="Refence file list")
@click.option(
    "--src_prefix",
    type=str,
    default='',
    help='Prefix of source file in command "ln -s [src] [dest]"',
)
@click.option(
    "--dst_prefix",
    type=str,
    default='',
    help='Prefix of destination file in command "ln -s [src] [dest]"',
)
def batch_symlink(files, src_prefix, dst_prefix):

    with open(files, "r") as fs:
        file_list = [line.rstrip() for line in fs]
        print("TOTAL: {} files".format(len(file_list)))
        errors = []
        cnt = 1
        for f in file_list:
            cmd = "ln -s {} {}".format(
                os.path.join(src_prefix, f), os.path.join(dst_prefix, f)
            )
            if os.system(cmd) == 0:
                print("[{}] SUCCEED: {}".format(cnt, cmd))
            else:
                errors.append(f)
                print("[{}] FAILED: {}".format(cnt, cmd))
            cnt += 1
        if errors:
            with open('errors.txt', 'w') as ef:
                for e in errors:
                    ef.write('{}\n'.format(e))
            print('Recorded {} errors in total.'.format(len(errors)))
        else:
            print('All done without exceptions!')


if __name__ == "__main__":
    batch_symlink()
