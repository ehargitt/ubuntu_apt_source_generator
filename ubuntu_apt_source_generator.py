def generate(version, arch_set):
    # (code_name, area_type)
    ubuntu_releases = {
        "5.04": ("hoary", "old"),
        "5.10": ("breezy", "old"),
        "6.06": ("dapper", "old"),
        "6.06.1": ("dapper", "old"),
        "6.06.2": ("dapper", "old"),
        "6.10": ("edgy", "old"),
        "7.04": ("feisty", "old"),
        "7.10": ("gutsy", "old"),
        "8.04": ("hardy", "old"),
        "8.04.1": ("hardy", "old"),
        "8.04.2": ("hardy", "old"),
        "8.04.3": ("hardy", "old"),
        "8.04.4": ("hardy", "old"),
        "8.10": ("intrepid", "old"),
        "9.04": ("jaunty", "old"),
        "9.10": ("karmic", "old"),
        "10.04": ("lucid", "old"),
        "10.04.1": ("lucid", "old"),
        "10.04.2": ("lucid", "old"),
        "10.04.3": ("lucid", "old"),
        "10.04.4": ("lucid", "old"),
        "10.10": ("maverick", "old"),
        "11.04": ("natty", "old"),
        "11.10": ("oneiric", "old"),
        "12.04": ("precise", "current"),
        "12.04.1": ("precise", "old"),
        "12.04.2": ("precise", "old"),
        "12.04.3": ("precise", "old"),
        "12.04.4": ("precise", "old"),
        "12.04.5": ("precise", "current"),
        "12.10": ("quantal", "old"),
        "13.04": ("raring", "old"),
        "13.10": ("saucy", "old"),
        "14.04": ("trusty", "old"),
        "14.04.1": ("trusty", "old"),
        "14.04.2": ("trusty", "old"),
        "14.04.3": ("trusty", "old"),
        "14.04.4": ("trusty", "old"),
        "14.04.5": ("trusty", "current"),
        "14.10": ("utopic", "old"),
        "15.04": ("vivid", "old"),
        "15.10": ("wily", "old"),
        "16.04": ("xenial", "current"),
        "16.04.1": ("xenial", "old"),
        "16.04.2": ("xenial", "old"),
        "16.04.3": ("xenial", "old"),
        "16.04.4": ("xenial", "old"),
        "16.04.5": ("xenial", "current"),
        "16.10": ("yakkety", "old"),
        "17.04": ("zesty", "old"),
        "17.10": ("artful", "old"),
        "18.04": ("bionic", "current"),
        "18.04.1": ("bionic", "current"),
        "18.10": ("cosmic", "current"),
    }

    components_string = 'main restricted universe multiverse'
    repos = ['security', 'updates']

    old_url = 'http://old-releases.ubuntu.com/ubuntu/'
    archive_url = 'http://archive.ubuntu.com/ubuntu/'
    port_url = 'http://ports.ubuntu.com/ubuntu-ports/'
    release = ubuntu_releases.get(version)

    # Prepare the architecture tags.
    native_arch_set = set()
    if 'amd64' in arch_set:
        native_arch_set.add('amd64')
    if 'i386' in arch_set:
        native_arch_set.add('i386')
    foreign_arch_set = arch_set - native_arch_set

    native_arch_tag = ''
    if native_arch_set:
        native_arch_string = ','.join([str(x) for x in native_arch_set])
        native_arch_tag = '[arch={0}]'.format(native_arch_string)

    foreign_arch_tag = ''
    if native_arch_set:
        foreign_arch_string = ','.join([str(x) for x in foreign_arch_set])
        foreign_arch_tag = '[arch={0}]'.format(foreign_arch_string)

    # Prepare the repository names.
    repo_names = ["{0}-{1}".format(release[0], x) for x in repos]
    repo_names.append(release[0])

    # Add all strings together to make full entries.
    prepared_entries = []
    if native_arch_set:
        if release[1] == 'current':
            url = archive_url
        elif release[1] == 'old':
            url = old_url
        else:
            raise Exception('Release area type "{}" is invalid'.format(release[1]))

        for name in repo_names:
            prepared_entries.append('deb {0} {1} {2} {3}'.format(native_arch_tag, url, name, components_string))

    if foreign_arch_set:
        if release[1] == 'current':
            url = port_url
        elif release[1] == 'old':
            url = old_url
        else:
            raise Exception('Release area type "{}" is invalid'.format(release[1]))

        for name in repo_names:
            prepared_entries.append('deb {0} {1} {2} {3}'.format(foreign_arch_tag, url, name, components_string))

    return prepared_entries


if __name__ == "__main__":
    archs = {'amd64', 'i386', 'armhf'}
    entries = generate('17.04', archs)
    print(entries)
