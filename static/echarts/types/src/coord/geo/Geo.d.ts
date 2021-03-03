import BoundingRect from 'zrender/lib/core/BoundingRect';
import View from '../View';
import Region from './Region';
import { NameMap } from './geoTypes';
import GlobalModel from '../../model/Global';
import { ParsedModelFinder } from '../../util/model';
import GeoModel from './GeoModel';
import { resizeGeoType } from './geoCreator';
declare class Geo extends View {
    dimensions: string[];
    type: string;
    readonly map: string;
    private _nameCoordMap;
    private _regionsMap;
    private _invertLongitute;
    readonly regions: Region[];
    aspectScale: number;
    model: GeoModel;
    resize: resizeGeoType;
    constructor(name: string, map: string, nameMap?: NameMap, invertLongitute?: boolean);
    containCoord(coord: number[]): boolean;
    transformTo(x: number, y: number, width: number, height: number): void;
    getRegion(name: string): Region;
    getRegionByCoord(coord: number[]): Region;
    addGeoCoord(name: string, geoCoord: number[]): void;
    getGeoCoord(name: string): number[];
    getBoundingRect(): BoundingRect;
    dataToPoint(data: number[], noRoam?: boolean, out?: number[]): number[];
    convertToPixel(ecModel: GlobalModel, finder: ParsedModelFinder, value: number[]): number[];
    convertFromPixel(ecModel: GlobalModel, finder: ParsedModelFinder, pixel: number[]): number[];
}
export default Geo;
