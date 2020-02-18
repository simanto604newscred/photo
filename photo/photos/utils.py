def image_path(instance, filename):
    root_dir = 'photos'
    return (
        f'{root_dir}/{instance.user.username}/{filename}'
    )
