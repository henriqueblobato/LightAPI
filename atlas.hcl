data "external_schema" "sqlalchemy" {
    program = [
        "python",
        "load_models.py"
    ]
}

env "sqlalchemy" {
    src = data.external_schema.sqlalchemy.url
    dev = "docker://mysql/8/dev"
}
