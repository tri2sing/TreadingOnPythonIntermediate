import os

def list_files_recurse(base_dir, recurse=True):
    '''Recursive function to get files in a directory.
    '''
    results = []
    for name in os.listdir(path=base_dir):
        filepath = os.path.join(base_dir, name)
        if os.path.isdir(filepath) and recurse:
            results.extend(list_files_recurse(filepath, recurse))
        else:
            results.append(filepath)
    return results


def list_files_yield(base_dir, recurse=True):
    '''Yield function to get files in a directory.
    '''
    for name in os.listdir(path=base_dir):
        filepath = os.path.join(base_dir, name)
        if os.path.isdir(filepath) and recurse:
            for child in list_files_yield(filepath, recurse):
                yield child
        else:
            yield filepath


if __name__ == '__main__':
    print(128*'=')
    print(128*'*')
    for path in list_files_recurse('/Users/sadhik1/Documents/wspython', recurse=True):
        print(path)
        
    print(128*'=')
    print(128*'*')
    for path in list_files_yield('/Users/sadhik1/Documents/wspython', recurse=True):
        print(path)
        