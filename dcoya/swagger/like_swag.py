post_swag = {
    "tags": ["Like"],
    "summary": "Create new blog post like",
    "description": "Create new blog post like.",
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

delete_swag = {
    "tags": ["Like"],
    "summary": "Delete like",
    "description": "Delete like by id.",
    "parameters": [
        {
            "in": "path",
            "name": "id",
            "required": True,
            "schema": {
                "type": "integer"
            },
            "description": "Like Id"
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

