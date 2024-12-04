post_swag = {
    "tags": ["Comment"],
    "summary": "Create new blog post comment",
    "description": "Create new blog post comment. Body minimum 10 characters",
    "parameters": [
        {
            "in": "path",
            "name": "post_id",
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
        "404": {
            "description": "Post not found"
        }
    }
}

put_swag = {
    "tags": ["Comment"],
    "summary": "Update Comment",
    "description": "Update comment by comment id. Body minimum 10 characters",
    "parameters": [
        {
            "in": "path",
            "name": "id",
            "required": True,
            "schema": {
                "type": "integer"
            },
            "description": "Comment Id"
        },
        {
            "in": "body",
            "name": "body",
            "required": True,
            "schema": {
                "properties": {
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

delete_swag = {
    "tags": ["Comment"],
    "summary": "Delete comment",
    "description": "Delete comment by id.",
    "parameters": [
        {
            "in": "path",
            "name": "id",
            "required": True,
            "schema": {
                "type": "integer"
            },
            "description": "Comment Id"
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

