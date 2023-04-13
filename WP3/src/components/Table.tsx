import { Condition, Display } from "@/types/GlobalTypes";
import {
  createColumnHelper,
  flexRender,
  getCoreRowModel,
  useReactTable,
} from "@tanstack/react-table";
import { useEffect, useRef } from "react";
import HideableElement from "./HideableElement";

const columnHelper = createColumnHelper<Display>();

const columns = [
  columnHelper.accessor("url", {
    header: () => "URL",
    cell: (info) => <a href={info.getValue()}>URL</a>,
  }),
  columnHelper.accessor("product_name", {
    header: () => "Product Name",
  }),
  columnHelper.accessor("generic_name", {
    header: () => "Generic Name",
  }),
  columnHelper.accessor("brands", {
    header: () => "Brands",
  }),
  columnHelper.accessor("categories_en", {
    header: () => "Categories (EN)",
  }),
  columnHelper.accessor("ingredients_text", {
    header: () => "Ingredients Text",
    cell: (info) => <HideableElement text={info.getValue()}/>,
  }),
  columnHelper.accessor("allergens", {
    header: () => "Allergens",
  }),
  columnHelper.accessor("serving_size", {
    header: () => "Serving Size",
  }),
  columnHelper.accessor("energy_100g", {
    header: () => "Energy (100g)",
  }),
  columnHelper.accessor("fat_100g", {
    header: () => "Fat (100g)",
  }),
  columnHelper.accessor("saturated_fat_100g", {
    header: () => "Saturated Fat (100g)",
  }),
  columnHelper.accessor("carbohydrates_100g", {
    header: () => "Carbohydrates (100g)",
  }),
  columnHelper.accessor("sugars_100g", {
    header: () => "Sugars (100g)",
  }),
  columnHelper.accessor("fiber_100g", {
    header: () => "Fiber (100g)",
  }),
  columnHelper.accessor("proteins_100g", {
    header: () => "Proteins (100g)",
  }),
  columnHelper.accessor("salt_100g", {
    header: () => "Salt (100g)",
  }),
  columnHelper.accessor("nutriscore_score", {
    header: () => "Nutriscore Score",
  }),
  columnHelper.accessor("nutriscore_grade", {
    header: () => "Nutriscore Grade",
  }),
  columnHelper.accessor("ecoscore_score", {
    header: () => "Ecoscore Score",
  }),
  columnHelper.accessor("ecoscore_grade", {
    header: () => "Ecoscore Grade",
  }),
];

export default function Table({ data }: { data: Display[] }) {
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
  });

  return (
    <div  className="p-2 w-full overflow-x-scroll scrollable-div rotate-180">
      <table className="-rotate-180">
        <thead>
          {table.getHeaderGroups().map((headerGroup) => (
            <tr key={headerGroup.id}>
              {headerGroup.headers.map((header) => (
                <th key={header.id}>
                  {header.isPlaceholder
                    ? null
                    : flexRender(
                        header.column.columnDef.header,
                        header.getContext()
                      )}
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody>
          {table.getRowModel().rows.map((row) => (
            <tr key={row.id}>
              {row.getVisibleCells().map((cell) => (
                <td className="border border-black text-center" key={cell.id}>
                  {flexRender(cell.column.columnDef.cell, cell.getContext())}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
        <tfoot>
          {table.getFooterGroups().map((footerGroup) => (
            <tr key={footerGroup.id}>
              {footerGroup.headers.map((header) => (
                <th key={header.id}>
                  {header.isPlaceholder
                    ? null
                    : flexRender(
                        header.column.columnDef.footer,
                        header.getContext()
                      )}
                </th>
              ))}
            </tr>
          ))}
        </tfoot>
      </table>
      <div className="h-4" />
    </div>
  );
}
