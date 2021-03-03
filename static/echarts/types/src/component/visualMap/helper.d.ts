import VisualMapModel from './VisualMapModel';
import ExtensionAPI from '../../core/ExtensionAPI';
import { Payload } from '../../util/types';
declare const paramsSet: readonly [readonly ["left", "right", "width"], readonly ["top", "bottom", "height"]];
export declare type ItemHorizontalAlign = typeof paramsSet[0][number];
export declare type ItemVerticalAlign = typeof paramsSet[1][number];
export declare type ItemAlign = ItemVerticalAlign | ItemHorizontalAlign;
export declare function getItemAlign(visualMapModel: VisualMapModel, api: ExtensionAPI, itemSize: number[]): ItemAlign;
export declare function makeHighDownBatch(batch: Payload['batch'], visualMapModel: VisualMapModel): Payload['batch'];
export {};
