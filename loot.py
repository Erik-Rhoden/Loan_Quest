import random

loot_map = {"Green Slime": {
                        "weapon": {
                                "Empty" : 0
                    },  "armor": {
                                "Empty": 0
                    },  "potion": {
                                "Empty": 0,
                    },  "misc": {
                                "Tattered Cloth": {
                                    "Useless": "Junk",
                                    "Value": 0.2,
                            },  "Animal Bones": {
                                    "Useless": "Junk",
                                    "Value": 0.2
                            },  "Slime Residue": {
                                    "Useless": "Junk",
                                    "Value": 0.2
                            },  "A Gold Piece": {
                                    "Gold": "Money",
                                    "Value": 1
                            },  "Human Skull": {
                                    "Useless": "Junk",
                                    "Value": 0.6
                            }
                    }},
            "Red Slime": {
                        "weapon": {
                                "Empty" : 0
                    },  "armor": {
                                "Empty": 0
                    },  "potion": {
                                "Empty": 0,
                    },  "misc": {
                                "Animal Bones": {
                                    "Useless": "Junk",
                                    "Value": 0.2
                            },  "Slime Residue": {
                                    "Useless": "Junk",
                                    "Value": 0.2,
                            },  "A Gold Piece": {
                                    "Gold": "Money",
                                    "Value": 1,
                            },  "Human Skull": {
                                    "Useless": "Junk",
                                    "Value": 0.6
                            },  "Shattered Dagger": {
                                    "Useless": "Junk",
                                    "Value": 2
                            }
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
                                "Slime Residue": {
                                    "Useless": "Junk",
                                    "Value": 0.2
                            },  "A Gold Piece": {
                                    "Gold": "Money",
                                    "Value": 1,
                            },  "Human Skull": {
                                    "Useless": "Junk",
                                    "Value": 0.6
                            },  "Shattered Dagger": {
                                    "Useless": "Junk",
                                    "Value": 2
                            },  "Broken Sword": {
                                    "Useless": "Junk",
                                    "Value": 3
                            }
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
                                "A Gold Piece": {
                                    "Gold": "Money",
                                    "Value": 1
                            },  "Human Skull": {
                                    "Useless": "Junk",
                                    "Value": 0.6
                            },  "Shattered Dagger": {
                                    "Useless": "Junk",
                                    "Value": 2
                            },  "Broken Shortsword": {
                                    "Useless": "Junk",
                                    "Value": 3
                            },  "Broken Bow": {
                                    "Useless": "Junk",
                                    "Value": 5
                            }
                    }},
            "Green Goblin": {
                        "weapon": {
                                "Empty" : 0,
                                "Club": {
                                    "Damage": 3,
                                    "Speed": 0,
                                    "Two-Hand": False,
                                    "Value": 3
                            },  "Dagger": {
                                    "Damage": 5,
                                    "Speed": 4,
                                    "Two-Hand": False,
                                    "Value": 5
                            }
                    },  "armor": {
                                "Empty": 0,
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Wool Shirt": {
                                    "Defense": 1,
                                    "Speed": 4,
                                    "Body": "Chest",
                                    "Value": 2
                            },  "Leather Cap": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Wooden Shield": {
                                    "Defense": 8,
                                    "Speed": 2,
                                    "Body": "Off-Hand",
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
                                "A Gold Piece": {
                                    "Gold": "Money",
                                    "Value": 1
                            },  "Shattered Dagger": {
                                    "Useless": "Junk",
                                    "Value": 2
                            },  "Broken Shortsword": {
                                    "Useless": "Junk",
                                    "Value": 3
                            },  "Broken Bow": {
                                    "Useless": "Junk",
                                    "Value": 5
                            },  "Broken Buckler": {
                                    "Useless": "Junk",
                                    "Value": 7
                            }
                    }},
            "Red Goblin": {
                        "weapon": {
                                "Empty" : 0,
                                "Club": {
                                    "Damage": 3,
                                    "Speed": 0,
                                    "Two-Hand": False,
                                    "Value": 3
                            },  "Dagger": {
                                    "Damage": 5,
                                    "Speed": 4,
                                    "Two-Hand": False,
                                    "Value": 5
                            },  "Shortsword": {
                                    "Damage": 10,
                                    "Speed": 2,
                                    "Two-Hand": False,
                                    "Value": 8
                            }
                    }, "armor": {
                                "Empty": 0,
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Wool Shirt": {
                                    "Defense": 1,
                                    "Speed": 4,
                                    "Body": "Chest",
                                    "Value": 2
                            },  "Leather Chest": {
                                    "Defense": 4,
                                    "Speed": 2,
                                    "Body": "Chest",
                                    "Value": 10
                            },  "Leather Pants": {
                                    "Defense": 4,
                                    "Speed": 2,
                                    "Body": "Legs",
                                    "Value": 10
                            },  "Wooden Shield": {
                                    "Defense": 8,
                                    "Speed": 2,
                                    "Body": "Off-Hand",
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
                                "A Gold Piece": {
                                    "Gold": "Money",
                                    "Value": 4
                            },  "Shattered Dagger": {
                                    "Useless": "Junk",
                                    "Value": 2
                            },  "Broken Shortsword": {
                                    "Useless": "Junk",
                                    "Value": 3
                            },  "Broken Bow": {
                                    "Useless": "Junk",
                                    "Value": 5
                            },  "Broken Buckler": {
                                    "Useless": "Junk",
                                    "Value": 7
                            }
                        }},
            "Silver Goblin": {
                        "weapon": {
                                "Club": {
                                    "Damage": 3,
                                    "Speed": 0,
                                    "Two-Hand": False,
                                    "Value": 3
                            },  "Dagger": {
                                    "Damage": 5,
                                    "Speed": 4,
                                    "Two-Hand": False,
                                    "Value": 5
                            },  "Shortsword": {
                                    "Damage": 10,
                                    "Speed": 2,
                                    "Two-Hand": False,
                                    "Value": 8
                            },  "Broadsword": {
                                    "Damage": 15,
                                    "Speed": -2,
                                    "Two-Hand": False,
                                    "Value": 30
                            }
                    }, "armor": {
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Leather Pants": {
                                    "Defense": 4,
                                    "Speed": 2,
                                    "Body": "Legs",
                                    "Value": 10
                            },  "Leather Chest": {
                                    "Defense": 4,
                                    "Speed": 2,
                                    "Body": "Chest",
                                    "Value": 10
                            },  "Leather Cap": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Iron Helm": {
                                    "Defense": 8,
                                    "Speed": -2,
                                    "Body": "Head",
                                    "Value": 20
                            },  "Wooden Shield": {
                                    "Defense": 8,
                                    "Speed": 2,
                                    "Body": "Off-Hand",
                                    "Value": 5
                            }
                    },  "potion": {
                                "Medium Health Potion": {
                                    "Heal": 20,
                                    "Value": 40
                            },  "Minor Health Potion": {
                                    "Heal": 5,
                                    "Value": 10
                            },  "Half-Full Medium Health Potion": {
                                    "Heal": 10,
                                    "Value": 20
                            }
                    },  "misc": {
                                "A Gold Piece": {
                                    "Gold": "Money",
                                    "Value": 4
                            },  "Merchant Crate": {
                                    "Useless": "Junk",
                                    "Value": 10
                            },  "Broken Shortsword": {
                                    "Useless": "Junk",
                                    "Value": 3
                            },  "Broken Bow": {
                                    "Useless": "Junk",
                                    "Value": 5
                            },  "Broken Buckler": {
                                    "Useless": "Junk",
                                    "Value": 7
                            }
                        }},
            "Golden Goblin": {
                        "weapon": {
                                "Shortsword": {
                                    "Damage": 10,
                                    "Speed": 2,
                                    "Two-Hand": False,
                                    "Value": 8
                            },  "Broadsword": {
                                    "Damage": 15,
                                    "Speed": -2,
                                    "Two-Hand": False,
                                    "Value": 30
                            },  "Longsword": {
                                    "Damage": 20,
                                    "Speed": -2,
                                    "Two-Hand": False,
                                    "Value": 50
                            }
                    },  "armor": {
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Leather Pants": {
                                    "Defense": 4,
                                    "Speed": 2,
                                    "Body": "Legs",
                                    "Value": 10
                            },  "Leather Chest": {
                                    "Defense": 4,
                                    "Speed": 2,
                                    "Body": "Chest",
                                    "Value": 10
                            },  "Leather Cap": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Wooden Shield": {
                                    "Defense": 8,
                                    "Speed": 2,
                                    "Body": "Off-Hand",
                                    "Value": 5
                            },  "Iron Boots": {
                                    "Defense": 7,
                                    "Speed": -2,
                                    "Body": "Feet",
                                    "Value": 15
                            },  "Iron Helm": {
                                    "Defense": 8,
                                    "Speed": -2,
                                    "Body": "Head",
                                    "Value": 20
                            },  "Iron Chest": {
                                    "Defense": 15,
                                    "Speed": -4,
                                    "Body": "Chest",
                                    "Value": 50
                            },  "Iron Shield": {
                                    "Defense": 20,
                                    "Speed": -5,
                                    "Body": "Off-Hand",
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
                                "A Gold Piece": {
                                    "Gold": "Money",
                                    "Value": 10
                            },  "Merchant Crate": {
                                    "Useless": "Junk",
                                    "Value": 10
                            },  "Golden Goblet": {
                                    "Useless": "Junk",
                                    "Value": 25
                            },  "Broken Bow": {
                                    "Useless": "Junk",
                                    "Value": 5
                            },  "Broken Buckler": {
                                    "Useless": "Junk",
                                    "Value": 7
                            }
                        }},
            "Green Orc": {
                        "weapon": {
                                "Broadsword": {
                                    "Damage": 15,
                                    "Speed": -2,
                                    "Two-Hand": False,
                                    "Value": 30
                            },  "Shortsword": {
                                    "Damage": 10,
                                    "Speed": 2,
                                    "Two-Hand": False,
                                    "Value": 8
                            },  "Longsword": {
                                    "Damage": 20,
                                    "Speed": -2,
                                    "Two-Hand": False,
                                    "Value": 50
                            },  "Stiletto": {
                                    "Damage": 10,
                                    "Speed": 8,
                                    "Two-Hand": False,
                                    "Value": 75
                            }
                    }, "armor": {
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Leather Pants": {
                                    "Defense": 4,
                                    "Speed": 2,
                                    "Body": "Legs",
                                    "Value": 10
                            },  "Leather Chest": {
                                    "Defense": 4,
                                    "Speed": 2,
                                    "Body": "Chest",
                                    "Value": 10
                            },  "Leather Cap": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Wooden Shield": {
                                    "Defense": 8,
                                    "Speed": 2,
                                    "Body": "Off-Hand",
                                    "Value": 5
                            },  "Iron Boots": {
                                    "Defense": 7,
                                    "Speed": -2,
                                    "Body": "Feet",
                                    "Value": 15
                            },  "Iron Leggings": {
                                    "Defense": 10,
                                    "Speed": -4,
                                    "Body": "Legs",
                                    "Value": 30
                            },  "Iron Chest": {
                                    "Defense": 15,
                                    "Speed": -4,
                                    "Body": "Chest",
                                    "Value": 50
                            },  "Iron Helm": {
                                    "Defense": 8,
                                    "Speed": -2,
                                    "Body": "Head",
                                    "Value": 20
                            },  "Iron Shield": {
                                    "Defense": 20,
                                    "Speed": -5,
                                    "Body": "Off-Hand",
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
                                "A Gold Piece": {
                                    "Gold": "Money",
                                    "Value": 15
                            },  "Merchant Crate": {
                                    "Useless": "Junk",
                                    "Value": 10
                            },  "Golden Goblet": {
                                    "Useless": "Junk",
                                    "Value": 25
                            },  "Broken Greatsword": {
                                    "Useless": "Junk",
                                    "Value": 15
                            },  "Broken Buckler": {
                                    "Useless": "Junk",
                                    "Value": 7
                            } 
                    }},
            "Red Orc": {
                        "weapon": {
                                "Broadsword": {
                                    "Damage": 15,
                                    "Speed": -2,
                                    "Two-Hand": False,
                                    "Value": 30
                            },  "Shortsword": {
                                    "Damage": 10,
                                    "Speed": 2,
                                    "Two-Hand": False,
                                    "Value": 8
                            },  "Longsword": {
                                    "Damage": 20,
                                    "Speed": -2,
                                    "Two-Hand": False,
                                    "Value": 50
                            },  "Stiletto": {
                                    "Damage": 10,
                                    "Speed": 8,
                                    "Two-Hand": False,
                                    "Value": 75
                            }
                    },  "armor": {
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Leather Pants": {
                                    "Defense": 4,
                                    "Speed": 2,
                                    "Body": "Legs",
                                    "Value": 10
                            },  "Leather Chest": {
                                    "Defense": 4,
                                    "Speed": 2,
                                    "Body": "Chest",
                                    "Value": 10
                            },  "Leather Cap": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Wooden Shield": {
                                    "Defense": 8,
                                    "Speed": 2,
                                    "Body": "Off-Hand",
                                    "Value": 5
                            },  "Iron Boots": {
                                    "Defense": 7,
                                    "Speed": -2,
                                    "Body": "Feet",
                                    "Value": 15
                            },  "Iron Leggings": {
                                    "Defense": 10,
                                    "Speed": -4,
                                    "Body": "Legs",
                                    "Value": 30
                            },  "Iron Chest": {
                                    "Defense": 15,
                                    "Speed": -4,
                                    "Body": "Chest",
                                    "Value": 50
                            },  "Iron Helm": {
                                    "Defense": 8,
                                    "Speed": -2,
                                    "Body": "Head",
                                    "Value": 20
                            },  "Iron Shield": {
                                    "Defense": 20,
                                    "Speed": -5,
                                    "Body": "Off-Hand",
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
                                "A Gold Piece": {
                                    "Gold": "Money",
                                    "Value": 15
                            },  "Merchant Crate": {
                                    "Useless": "Junk",
                                    "Value": 10
                            },  "Golden Goblet": {
                                    "Useless": "Junk",
                                    "Value": 25
                            },  "Broken Greatsword": {
                                    "Useless": "Junk",
                                    "Value": 15
                            },  "Bent Mage Staff": {
                                    "Useless": "Junk",
                                    "Value": 20
                            }
                    }},
            "Silver Orc": {
                        "weapon": {
                                "Broadsword": {
                                    "Damage": 15,
                                    "Speed": -2,
                                    "Two-Hand": False,
                                    "Value": 30
                            },  "Shortsword": {
                                    "Damage": 10,
                                    "Speed": 2,
                                    "Two-Hand": False,
                                    "Value": 8
                            },  "Longsword": {
                                    "Damage": 20,
                                    "Speed": -2,
                                    "Two-Hand": False,
                                    "Value": 50
                            },  "Stiletto": {
                                    "Damage": 10,
                                    "Speed": 8,
                                    "Two-Hand": False,
                                    "Value": 75
                            }
                    }, "armor": {
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Leather Pants": {
                                    "Defense": 4,
                                    "Speed": 2,
                                    "Body": "Legs",
                                    "Value": 10
                            },  "Leather Chest": {
                                    "Defense": 4,
                                    "Speed": 2,
                                    "Body": "Chest",
                                    "Value": 10
                            },  "Leather Cap": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Wooden Shield": {
                                    "Defense": 8,
                                    "Speed": 2,
                                    "Body": "Off-Hand",
                                    "Value": 5
                            },  "Iron Boots": {
                                    "Defense": 7,
                                    "Speed": -2,
                                    "Body": "Feet",
                                    "Value": 15
                            },  "Iron Leggings": {
                                    "Defense": 10,
                                    "Speed": -4,
                                    "Body": "Legs",
                                    "Value": 30
                            },  "Iron Chest": {
                                    "Defense": 15,
                                    "Speed": -4,
                                    "Body": "Chest",
                                    "Value": 50
                            },  "Iron Helm": {
                                    "Defense": 8,
                                    "Speed": -2,
                                    "Body": "Head",
                                    "Value": 20
                            },  "Iron Shield": {
                                    "Defense": 20,
                                    "Speed": -5,
                                    "Body": "Off-Hand",
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
                                "A Gold Piece": {
                                    "Gold": "Money",
                                    "Value": 15
                            },  "King's Crate": {
                                    "Useless": "Junk",
                                    "Value": 50
                            },  "Golden Goblet": {
                                    "Useless": "Junk",
                                    "Value": 25
                            },  "Broken Greatsword": {
                                    "Useless": "Junk",
                                    "Value": 15
                            },  "Bent Mage Staff": {
                                    "Useless": "Junk",
                                    "Value": 20
                            }
                    }},
            "Golden Orc": {
                        "weapon": {
                                "Broadsword": {
                                    "Damage": 15,
                                    "Speed": -2,
                                    "Two-Hand": False,
                                    "Value": 30
                            },  "Greatsword": {
                                    "Damage": 40,
                                    "Speed": -6,
                                    "Two-Hand": True,
                                    "Value": 100
                            },  "Longsword": {
                                    "Damage": 20,
                                    "Speed": -2,
                                    "Two-Hand": False,
                                    "Value": 50
                            },  "Stiletto": {
                                    "Damage": 10,
                                    "Speed": 8,
                                    "Two-Hand": False,
                                    "Value": 75
                            }
                    },  "armor": {
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Leather Pants": {
                                    "Defense": 4,
                                    "Speed": 2,
                                    "Body": "Legs",
                                    "Value": 10
                            },  "Leather Chest": {
                                    "Defense": 4,
                                    "Speed": 2,
                                    "Body": "Chest",
                                    "Value": 10
                            },  "Leather Cap": {
                                    "Defense": 1,
                                    "Speed": 2,
                                    "Body": "Feet",
                                    "Value": 3
                            },  "Wooden Shield": {
                                    "Defense": 8,
                                    "Speed": 2,
                                    "Body": "Off-Hand",
                                    "Value": 5
                            },  "Iron Boots": {
                                    "Defense": 7,
                                    "Speed": -2,
                                    "Body": "Feet",
                                    "Value": 15
                            },  "Iron Leggings": {
                                    "Defense": 10,
                                    "Speed": -4,
                                    "Body": "Legs",
                                    "Value": 30
                            },  "Iron Chest": {
                                    "Defense": 15,
                                    "Speed": -4,
                                    "Body": "Chest",
                                    "Value": 50
                            },  "Iron Helm": {
                                    "Defense": 8,
                                    "Speed": -2,
                                    "Body": "Head",
                                    "Value": 20
                            },  "Steel Shield": {
                                    "Defense": 35,
                                    "Speed": -10,
                                    "Body": "Off-Hand",
                                    "Value": 100
                            },  "Steel Helm": {
                                    "Defense": 15,
                                    "Speed": -4,
                                    "Body": "Head",
                                    "Value": 40
                            },  "Steel Boots": {
                                    "Defense": 15,
                                    "Speed": -4,
                                    "Body": "Feet",
                                    "Value": 30
                            },  "Steel Leggings": {
                                    "Defense": 20,
                                    "Speed": -8,
                                    "Body": "Legs",
                                    "Value": 60
                            },  "Steel Chest": {
                                    "Defense": 30,
                                    "Speed": -8,
                                    "Body": "Chest",
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
                                "A Gold Piece": {
                                    "Gold": "Money",
                                    "Value": 50
                            },  "King's Crate": {
                                    "Useless": "Junk",
                                    "Value": 50
                            },  "Diamond Necklace": {
                                    "Useless": "Junk",
                                    "Value": 100
                            },  "Broken Greatsword": {
                                    "Useless": "Junk",
                                    "Value": 15
                            },  "Bent Mage Staff": {
                                    "Useless": "Junk",
                                    "Value": 20
                            } 
                    }},
        }

class Item():
    def __init__(self, name, type, value, capacity=None):
        self.name = name
        self.type = type
        self.value = value
        self.capacity = capacity

    def __repr__(self):
        return f"{self.name}({self.type}) - Value: {self.value}"

class Weapon(Item):
    def __init__(self, name, type, value, damage, speed, two_hand=False):
        super().__init__(name, type, value)
        self.damage = damage
        self.speed = speed
        self.two_hand = two_hand

    def __repr__(self):
        return f"{self.name}({self.type}) - Damage: {self.damage} - Value: {self.value}"

class Armor(Item):
    def __init__(self, name, type, value, defense, speed, body_type):
        super().__init__(name, type, value)
        self.body_type = body_type
        self.speed = speed
        self.defense = defense

    def __repr__(self):
        return f"{self.name}({self.type}) - Defense: {self.defense} - Value: {self.value}"

class Potion(Item):
    def __init__(self, name, type, value, heal):
        super().__init__(name, type, value)
        self.heal = heal

    def __repr__(self):
        return f"{self.name}({self.type}) - Heals: {self.heal} - Value: {self.value}"