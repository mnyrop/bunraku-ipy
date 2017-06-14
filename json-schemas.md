# json schemas:

#### authors:
```json
{
    "id": "PRIMARY-KEY",

    "label_eng": "STRING",
    "label_ka": "STRING",
    "dates": "STRING",
    "reference": "STRING",
    "sort_ja": "STRING",

    "play_id": ["ID ARRAY"]
}
```

#### characters:
```json
{
    "id": "PRIMARY-KEY",

    "character_code": "STRING",
    "label_eng": "STRING",
    "label_ja": "STRING",
    "label_ka": "STRING",
    "authority_control": "STRING",
    "sort_ja": "STRING",

    "play_id": ["ID ARRAY"],
    "image_id": ["ID ARRAY"]
}
```

#### images:
```json
{
    "id": "PRIMARY-KEY",

    "media_type": "STRING",
    "container": "STRING",
    "container_type":"STRING",
    "creator": "STRING",
    "item_id": "STRING",
    "colser_id": "STRING",
    "notes": "STRING",
    "objid": "STRING",
    "sequence": "STRING",
    "series": "STRING",
    "slidepage_folder": "STRING",

    "character_id": ["ID ARRAY"],
    "tag_id": ["ID ARRAY"],
    "kashira_id": ["ID ARRAY"],
    "performance_id": ["ID ARRAY"],
    "performer_id": ["ID ARRAY"],
    "play_id": ["ID ARRAY"],
    "production_id": ["ID ARRAY"],
    "scene_id": ["ID ARRAY"]

}
```

#### tags:
```json
{
    "id": "PRIMARY-KEY",

    "label_eng": "STRING",
    "label_ka": "STRING",
    "description": "STRING",
    "notes": "STRING",
    "sort_ja": "STRING",

    "image_id": ["ID ARRAY"]
}
```

#### kashira:
```json
{
    "id": "PRIMARY-KEY",

    "label_eng": "STRING",
    "label_ka": "STRING",
    "category": "STRING",
    "sort_ja": "STRING",

    "image_id": ["ID ARRAY"]
}
```

#### performances:
```json
{
    "id": "PRIMARY-KEY",
    "play_id": ["ID ARRAY"],
    "production_id": ["ID ARRAY"],
    "performance_scene_id": ["ID ARRAY"],
    "character_id": ["ID ARRAY"],
    "image_id": ["ID ARRAY"]
}
```

#### plays:  
```json
  {
      "id": "PRIMARY-KEY",

      "label_ja": "STRING",
      "label_ja_sort": "STRING",
      "label_ka": "STRING",
      "sort_ja": "STRING",
      "label_eng": "STRING",
      "label_eng_sort": "STRING",
      "first_staged": "STRING",
      "reference": "STRING",

      "author_id": ["ID ARRAY"],
      "character_id": ["ID ARRAY"],
      "image_id": ["ID ARRAY"],
      "performance_id": ["ID ARRAY"]
  }
  ```

  #### productions:  
  ```json
    {
        "id": "PRIMARY-KEY",

        "dates": "STRING",
        "place": "STRING",
        "label_eng": "STRING",

        "image_id": ["ID ARRAY"],
        "performance_id": ["ID ARRAY"],
        "play_id": ["ID ARRAY"]
    }
    ```
