import random

loot_map = {"Green Slime": {
                        "weapon": {
                                "Empty" : 0
                    },  "armor": {
                                "Empty": 0
                    },  "potion": {
                                "Empty": 0,
                    },  "misc": {
                                "Tattered Cloth": 0.1,
                                "Animal Bones": 0.2,
                                "Slime Residue": 0.1,
                                "A Gold Piece": 1,
                                "Human Skull": 0.5
                    }},
            "Red Slime": {
                        "weapon": {
                                "Empty" : 0
                    },  "armor": {
                                "Empty": 0
                    },  "potion": {
                                "Empty": 0,
                    },  "misc": {
                                "Animal Bones": 0.2,
                                "Slime Residue": 0.1,
                                "A Gold Piece": 1,
                                "Human Skull": 0.5,
                                "Shattered Dagger": 2.0,
                    }},
            "Silver Slime": {
                        "weapon": {
                                "Empty" : 0
                    },  "armor": {
                                "Empty": 0
                    },  "potion": {
                                "Empty": 0,
                                "Half-Full Minor Health Potion": {
                                    "Heal": 3,
                                    "Value": 5
                                }
                    },  "misc": {
                                "Slime Residue": 0.1,
                                "A Gold Piece": 1,
                                "Human Skull": 0.5,
                                "Shattered Dagger": 2.0,
                                "Broken Sword": 3.0,
                    }},
            "Golden Slime": {
                        "weapon": {
                                "Empty" : 0
                    },  "armor": {
                                "Empty": 0
                    },  "potion": {
                                "Empty": 0,
                                "Half-Full Minor Health Potion": {
                                    "Heal": 3,
                                    "Value": 5
                            },  "Minor Health Potion": {
                                    "Heal": 5,
                                    "Value": 10,
                            },  "Half-Full Medium Health Potion": {
                                    "Heal": 10,
                                    "Value": 20,
                            }
                    },  "misc": {
                                "A Gold Piece": 1,
                                "Human Skull": 0.5,
                                "Shattered Dagger": 2.0,
                                "Broken Shortsword": 3.0,
                                "Broken Bow": 5.0 
                    }},
            "Green Goblin": {
                        "weapon": {
                                "Empty" : 0,
                                "Club": {
                                    "Damage": 2,
                                    "Value": 3
                            },  "Dagger": {
                                    "Damage": 5,
                                    "Value": 5
                            }
                    },  "armor": {
                                "Empty": 0,
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Value": 3
                            },  "Wool Shirt": {
                                    "Defense": 1,
                                    "Value": 2
                            },  "Wooden Shield": {
                                    "Defense": 8,
                                    "Value": 5
                            }
                    },  "potion": {
                                "Empty": 0,
                                "Half-Full Minor Health Potion": {
                                    "Heal": 3,
                                    "Value": 5
                            },  "Minor Health Potion": {
                                    "Heal": 5,
                                    "Value": 10,
                            },
                    },  "misc": {
                                "A Gold Piece": 1,
                                "Shattered Dagger": 2.0,
                                "Broken Shortsword": 3.0,
                                "Broken Bow": 5.0,
                                "Broken Buckler": 7.5 
                    }},
            "Red Goblin": {
                        "weapon": {
                                "Empty" : 0,
                                "Club": {
                                    "Damage": 2,
                                    "Value": 3
                            },  "Dagger": {
                                    "Damage": 5,
                                    "Value": 5
                            },  "Shortsword": {
                                    "Damage": 10,
                                    "Value": 8
                            }
                    }, "armor": {
                                "Empty": 0,
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Value": 3
                            },  "Wool Shirt": {
                                    "Defense": 1,
                                    "Value": 2
                            },  "Leather Chest": {
                                    "Defense": 4,
                                    "Value": 10
                            },  "Leather Pants": {
                                    "Defense": 4,
                                    "Value": 10
                            },  "Wooden Shield": {
                                    "Defense": 8,
                                    "Value": 5
                            }
                    },  "potion": {
                                "Half-Full Minor Health Potion": {
                                    "Heal": 3,
                                    "Value": 5
                            },  "Minor Health Potion": {
                                    "Heal": 5,
                                    "Value": 10,
                            },  "Half-Full Medium Health Potion": {
                                    "Heal": 10,
                                    "Value": 20,
                            }
                    },  "misc": {
                                "Gold Pieces": 4,
                                "Shattered Dagger": 2.0,
                                "Broken Shortsword": 3.0,
                                "Broken Bow": 5.0,
                                "Broken Buckler": 7.5
                        }},
            "Silver Goblin": {
                        "weapon": {
                                "Club": {
                                    "Damage": 2,
                                    "Value": 3
                            },  "Dagger": {
                                    "Damage": 5,
                                    "Value": 5
                            },  "Shortsword": {
                                    "Damage": 10,
                                    "Value": 8
                            },  "Broadsword": {
                                    "Damage": 15,
                                    "Value": 30
                            }
                    }, "armor": {
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Value": 3
                            },  "Leather Pants": {
                                    "Defense": 4,
                                    "Value": 10
                            },  "Leather Chest": {
                                    "Defense": 4,
                                    "Value": 10
                            },  "Iron Helm": {
                                    "Defense": 8,
                                    "Value": 20
                            },  "Wooden Shield": {
                                    "Defense": 8,
                                    "Value": 5
                            }
                    },  "potion": {
                                "Medium Health Potion": {
                                    "Heal": 20,
                                    "Value": 40
                            },  "Minor Health Potion": {
                                    "Heal": 5,
                                    "Value": 10,
                            },  "Half-Full Medium Health Potion": {
                                    "Heal": 10,
                                    "Value": 20,
                            }
                    },  "misc": {
                                "Gold Pieces": 4,
                                "Merchant Crate": 10,
                                "Broken Shortsword": 3.0,
                                "Broken Bow": 5.0,
                                "Broken Buckler": 7.5
                        }},
            "Golden Goblin": {
                        "weapon": {
                                "Shortsword": {
                                    "Damage": 10,
                                    "Value": 8
                            },  "Broadsword": {
                                    "Damage": 15,
                                    "Value": 30
                            },  "Longsword": {
                                    "Damage": 20,
                                    "Value": 50
                            }
                    },  "armor": {
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Value": 3
                            },  "Leather Pants": {
                                    "Defense": 4,
                                    "Value": 10
                            },  "Leather Chest": {
                                    "Defense": 4,
                                    "Value": 10
                            },  "Iron Boots": {
                                    "Defense": 7,
                                    "Value": 15
                            },  "Iron Helm": {
                                    "Defense": 8,
                                    "Value": 20
                            },  "Iron Chest": {
                                    "Defense": 15,
                                    "Value": 50
                            },  "Iron Shield": {
                                    "Defense": 20,
                                    "Value": 30
                            }
                    },  "potion": {
                                "Medium Health Potion": {
                                    "Heal": 20,
                                    "Value": 40
                            },  "Minor Health Potion": {
                                    "Heal": 5,
                                    "Value": 10,
                            },  "Half-Full Medium Health Potion": {
                                    "Heal": 10,
                                    "Value": 20,
                            },  "Half-Full High Health Potion": {
                                    "Heal": 40,
                                    "Value": 50
                            }
                    },  "misc": {
                                "Gold Pieces": 10,
                                "Merchant Crate": 10,
                                "Golden Goblet": 25.0,
                                "Broken Bow": 5.0,
                                "Broken Buckler": 7.5
                        }},
            "Green Orc": {
                        "weapon": {
                                "Broadsword": {
                                    "Damage": 15,
                                    "Value": 30
                            },  "Shortsword": {
                                    "Damage": 10,
                                    "Value": 8
                            },  "Longsword": {
                                    "Damage": 20,
                                    "Value": 50
                            }
                    }, "armor": {
                                "Iron Boots": {
                                    "Defense": 7,
                                    "Value": 15
                            },  "Iron Leggings": {
                                    "Defense": 10,
                                    "Value": 30
                            },  "Iron Chest": {
                                    "Defense": 15,
                                    "Value": 50
                            },  "Iron Helm": {
                                    "Defense": 8,
                                    "Value": 20
                            },  "Iron Shield": {
                                    "Defense": 20,
                                    "Value": 30
                            }
                    },  "potion": {
                                "Medium Health Potion": {
                                    "Heal": 20,
                                    "Value": 40
                            },  "Minor Health Potion": {
                                    "Heal": 5,
                                    "Value": 10,
                            },  "Half-Full Medium Health Potion": {
                                    "Heal": 10,
                                    "Value": 20,
                            },  "Half-Full High Health Potion": {
                                    "Heal": 40,
                                    "Value": 50
                            }
                    },  "misc": {
                                "Gold Pieces": 15,
                                "Merchant Crate": 10,
                                "Golden Goblet": 25.0,
                                "Broken Greatsword": 15.0,
                                "Broken Buckler": 7.5 
                    }},
            "Red Orc": {
                        "weapon": {
                                "Broadsword": {
                                    "Damage": 15,
                                    "Value": 30
                            },  "Shortsword": {
                                    "Damage": 10,
                                    "Value": 8
                            },  "Longsword": {
                                    "Damage": 20,
                                    "Value": 50
                            }
                    }, "armor": {
                                "Iron Boots": {
                                    "Defense": 7,
                                    "Value": 15
                            },  "Iron Leggings": {
                                    "Defense": 10,
                                    "Value": 30
                            },  "Iron Chest": {
                                    "Defense": 15,
                                    "Value": 50
                            },  "Iron Helm": {
                                    "Defense": 8,
                                    "Value": 20
                            },  "Iron Shield": {
                                    "Defense": 20,
                                    "Value": 30
                            }
                    },  "potion": {
                                "Medium Health Potion": {
                                    "Heal": 20,
                                    "Value": 40
                            },  "Minor Health Potion": {
                                    "Heal": 5,
                                    "Value": 10,
                            },  "Half-Full Medium Health Potion": {
                                    "Heal": 10,
                                    "Value": 20,
                            },  "Half-Full High Health Potion": {
                                    "Heal": 40,
                                    "Value": 50
                            }
                    },  "misc": {
                                "Gold Pieces": 15,
                                "Merchant Crate": 10,
                                "Golden Goblet": 25.0,
                                "Broken Greatsword": 15.0,
                                "Bent Mage Staff": 20.0
                        }},
            "Silver Orc": {
                        "weapon": {
                                "Broadsword": {
                                    "Damage": 15,
                                    "Value": 30
                            },  "Shortsword": {
                                    "Damage": 10,
                                    "Value": 8
                            },  "Longsword": {
                                    "Damage": 20,
                                    "Value": 50
                            }
                    }, "armor": {
                                "Iron Boots": {
                                    "Defense": 7,
                                    "Value": 15
                            },  "Iron Leggings": {
                                    "Defense": 10,
                                    "Value": 30
                            },  "Iron Chest": {
                                    "Defense": 15,
                                    "Value": 50
                            },  "Iron Helm": {
                                    "Defense": 8,
                                    "Value": 20
                            },  "Steel Shield": {
                                    "Defense": 35,
                                    "Value": 100
                            },  "Iron Shield": {
                                    "Defense": 20,
                                    "Value": 30
                            }
                    },  "potion": {
                                "Medium Health Potion": {
                                    "Heal": 20,
                                    "Value": 40
                            },  "High Health Potion": {
                                    "Heal": 80,
                                    "Value": 100
                            },  "Half-Full Medium Health Potion": {
                                    "Heal": 10,
                                    "Value": 20,
                            },  "Half-Full High Health Potion": {
                                    "Heal": 40,
                                    "Value": 50
                            }
                    },  "misc": {
                                "Gold Pieces": 15,
                                "King's Crate": 50,
                                "Golden Goblet": 25.0,
                                "Broken Greatsword": 15.0,
                                "Bent Mage Staff": 20.0
                    }},
            "Golden Orc": {
                        "weapon": {
                                "Broadsword": {
                                    "Damage": 15,
                                    "Value": 30
                            },  "Greatsword": {
                                    "Damage": 40,
                                    "Value": 100
                            },  "Longsword": {
                                    "Damage": 20,
                                    "Value": 50
                            }
                    },  "armor": {
                                "Iron Boots": {
                                    "Defense": 7,
                                    "Value": 15
                            },  "Iron Leggings": {
                                    "Defense": 10,
                                    "Value": 30
                            },  "Iron Chest": {
                                    "Defense": 15,
                                    "Value": 50
                            },  "Iron Helm": {
                                    "Defense": 8,
                                    "Value": 20
                            },  "Steel Shield": {
                                    "Defense": 35,
                                    "Value": 100
                            },  "Steel Helm": {
                                    "Defense": 15,
                                    "Value": 40
                            },  "Steel Boots": {
                                    "Defense": 15,
                                    "Value": 30
                            },  "Steel Leggings": {
                                    "Defense": 20,
                                    "Value": 60
                            },  "Steel Chest": {
                                    "Defense": 30,
                                    "Value": 100
                            }
                    },  "potion": {
                                "Medium Health Potion": {
                                    "Heal": 20,
                                    "Value": 40
                            },  "High Health Potion": {
                                    "Heal": 80,
                                    "Value": 100
                            },  "Half-Full High Health Potion": {
                                    "Heal": 40,
                                    "Value": 50
                            }
                    },  "misc": {
                                "Gold Pieces": 50,
                                "King's Crate": 50,
                                "Diamond Necklace": 100.0,
                                "Broken Greatsword": 15.0,
                                "Bent Mage Staff": 20.0 
                    }},
        }