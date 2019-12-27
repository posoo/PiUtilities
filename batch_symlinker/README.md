# BatchSymlinker

There are a lot of files need keeping syncing in some folders. However, I want some of them to be indexed by my media services, which requires these files are able to be accessed in some specific directories. Thus I often need to manually make some symbolic links based on different rules. These two scripts can increase my efficiency by soft linking a batch of files in terms of date interval.

You need to install [click](https://pypi.org/project/click/) first.

## Usage

- Run `date_filter.py` first to generate a list of files from the date interval given by you.
- Then you can edit the generated file list to confirm it consistent with your intention. 
- Run `batch_symlink.py` to soft link them. Failed cases will be recorded in `errors.txt` in the current directory.

More details of arguments in both scripts can be checked by `--help`.