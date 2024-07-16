import random

loot_map = {"Green Slime": {
                        "weapon": {
                            "Empty" : 0
                    }, "armor": {
                            "Empty": 0
                    },
                        "misc": {
                                "Tattered Cloth": 0.1,
                                "Animal Bones": 0.2,
                                "Slime Residue": 0.1,
                                "A Gold Piece": 1,
                                "Human Skull": 0.5
                    }},
            "Red Slime": {
                        "weapon": {
                            "Empty" : 0
                        }, "armor": {
                                "Empty": 0
                        },
                            "misc": {
                                "Animal Bones": 0.2,
                                "Slime Residue": 0.1,
                                "A Gold Piece": 1,
                                "Human Skull": 0.5,
                                "Shattered Dagger": 2.0,
                    }},
            "Silver Slime": {
                        "weapon": {
                            "Empty" : 0
                    }, "armor": {
                            "Empty": 0
                    },
                        "misc": {
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
                                "Half-Full Minor Health Potion": 5,
                                "Minor Health Potion": 10,
                                "Half-Full Medium Health Potion": 20
                    },
                        "misc": {
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
                            },
                            "Dagger": {
                                "Damage": 5,
                                "Value": 5
                            }
                    }, "armor": {
                                "Empty": 0,
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Value": 3
                                },
                                "Wool Shirt": {
                                    "Defense": 1,
                                    "Value": 2
                                }
                    },  "potion": {
                                "Empty": 0,
                                "Half-Full Minor Health Potion": 5,
                                "Minor Health Potion": 10,
                    },    
                        "misc": {
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
                            },
                            "Dagger": {
                                "Damage": 5,
                                "Value": 5
                            },
                            "Shortsword": {
                                "Damage": 10,
                                "Value": 8
                            }
                    }, "armor": {
                                "Empty": 0,
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Value": 3
                                },
                                "Wool Shirt": {
                                    "Defense": 1,
                                    "Value": 2
                                },
                                "Leather Chest": {
                                    "Defense": 4,
                                    "Value": 10
                                }
                    },  "potion": {
                                "Half-Full Minor Health Potion": 5,
                                "Minor Health Potion": 10,
                                "Half-Full Medium Health Potion": 20
                    },
                        "misc": {
                                "Gold Pieces": 4,
                                "Shattered Dagger": 2.0,
                                "Broken Shortsword": 3.0,
                                "Broken Bow": 5.0,
                                "Broken Buckler": 7.5
                        }},
            "Silver Goblin": {
                        "weapon": {
                            "Empty" : 0
                    }, "armor": {
                                "Empty": 0,
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Value": 3
                                },
                                "Wool Shirt": {
                                    "Defense": 1,
                                    "Value": 2
                                },
                                "Leather Chest": {
                                    "Defense": 4,
                                    "Value": 10
                                },
                                "Iron Helm": {
                                    "Defense": 8,
                                    "Value": 20
                                }
                    },
                        "misc": {
                                "Gold Pieces": 4,
                                "Merchant Crate": 10,
                                "Broken Shortsword": 3.0,
                                "Broken Bow": 5.0,
                                "Broken Buckler": 7.5
                        }},
            "Golden Goblin": {
                        "weapon": {
                            "Empty" : 0
                    },  "armor": {
                                "Empty": 0,
                                "Leather Shoes": {
                                    "Defense": 1,
                                    "Value": 3
                                },
                                "Wool Shirt": {
                                    "Defense": 1,
                                    "Value": 2
                                },
                                "Leather Chest": {
                                    "Defense": 4,
                                    "Value": 10
                                },
                                "Iron Helm": {
                                    "Defense": 8,
                                    "Value": 20
                                },
                                "Iron Chest": {
                                    "Defense": 15,
                                    "Value": 50
                                }
                    },  "potion": {
                                "Medium Health Potion": 40,
                                "Half-Full Minor Health Potion": 5,
                                "Minor Health Potion": 10,
                                "Half-Full Medium Health Potion": 20
                    },
                        "misc": {
                                "Gold Pieces": 4,
                                "Merchant Crate": 10,
                                "Golden Goblet": 25.0,
                                "Broken Bow": 5.0,
                                "Broken Buckler": 7.5 
                        }},
            }

print(loot_map["Golden Goblin"]["armor"]["Iron Chest"]["Value"])