/**
 * Tipos TypeScript para A Life's Random Journey
 */

// Tipo para nodos narrativos
export interface GameNode {
  id: string;
  type: 'start' | 'event' | 'decision' | 'end';
  location_arc?: string;
  title: string;
  image?: string;
  text: string;
  music?: string;
  sfx?: string;
  options: GameOption[];
  effects?: GameEffects;
  npcs_present?: string[];
}

// Tipo para opciones de decisión
export interface GameOption {
  text: string;
  next_node_id: string;
  conditions?: any;
}

// Tipo para efectos de eventos
export interface GameEffects {
  health_change?: number;
  money_change?: number;
  memory_add?: string;
  [key: string]: any;
}

// Tipo para el estado del personaje
export interface Character {
  id: string;
  name: string;
  gender: string;
  age: number;
  health: number;
  money: number;
  location: string;
  memories: string[];
  current_node: string;
}

// Tipo para NPCs
export interface NPC {
  id: string;
  name: string;
  description: string;
  location: string;
  alive: boolean;
  relationship_with_player: number;
}

// Tipo para el estado del juego
export interface GameState {
  character: Character;
  current_node: GameNode;
  npcs: NPC[];
  world_state: any;
} 