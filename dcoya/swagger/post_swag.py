get_swag = {
    "tags": ["Post"],
    "summary": "Get one post",
    "description": "Get one post by post id.",
    "parameters": [
        {
            "in": "path",
            "name": "id",
            "required": True,
            "schema": {
                "type": "integer"
            },
            "description": "Post Id"
        },
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": False,
            "description": "Optional"
        }
    ],
    "responses": {
        "200": {
            "description": "Success"
        },
        "400": {
            "description": "Invalid data"
        },
        "404": {
            "description": "Post not found"
        }
    }
}

get_all_swag = {
    "tags": ["Post"],
    "summary": "All posts",
    "description": "Get all posts.",
    "responses": {
        "200": {
            "description": "Success"
        },
        "400": {
            "description": "Invalid data"
        }
    }
}

put_swag = {
    "tags": ["Post"],
    "summary": "Update Post",
    "description": "Update post by post id. Can be updated or title or body or both. Title between 3 and 200 characters. Body minimum 50 characters",
    "parameters": [
        {
            "in": "path",
            "name": "id",
            "required": True,
            "schema": {
                "type": "integer"
            },
            "description": "Post Id"
        },
        {
            "in": "body",
            "name": "body",
            "required": True,
            "schema": {
                "properties": {
                    "title": {"type": "string", "required": False},
                    "body": {"type": "string", "required": False}
                }
            }
        },
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True
        }
    ],
    "responses": {
        "200": {
            "description": "Success"
        },
        "400": {
            "description": "Invalid data"
        },
        "401": {
            "description": "Unauthorized"
        },
        "404": {
            "description": "Not found"
        }
    }
}

post_swag = {
    "tags": ["Post"],
    "summary": "Create new blog post",
    "description": "Create new blog post. Title between 3 and 200 characters. Body minimum 50 characters",
    "parameters": [
        {
            "in": "body",
            "name": "body",
            "required": True,
            "schema": {
                "properties": {
                    "title": {"type": "string"},
                    "body": {"type": "string"}
                }
            }
        },
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True
        }
    ],
    "responses": {
        "200": {
            "description": "Success"
        },
        "400": {
            "description": "Invalid data"
        },
        "401": {
            "description": "Unauthorized"
        },
    }
}

delete_swag = {
    "tags": ["Post"],
    "summary": "Delete post",
    "description": "Delete post by id.",
    "parameters": [
        {
            "in": "path",
            "name": "id",
            "required": True,
            "schema": {
                "type": "integer"
            },
            "description": "Post Id"
        },
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
        }
    ],
    "responses": {
        "200": {
            "description": "Success"
        },
        "400": {
            "description": "Invalid data"
        },
        "401": {
            "description": "Unauthorized"
        },
        "404": {
            "description": "Post not found"
        }
    }
}
